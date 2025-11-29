import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np

# Load sentence transformer model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Global data storage
DATA = {
    "customers": None,
    "products": None,
    "purchases": None,
    "reviews": None,
    "offers": None
}

# Global index storage
INDEX = {
    "product_embeddings": None,
    "offer_embeddings": None,
    "customer_profiles": None
}

def load_csvs(cust, prod, purch, rev, off):
    DATA["customers"] = cust
    DATA["products"] = prod
    DATA["purchases"] = purch
    DATA["reviews"] = rev
    DATA["offers"] = off

def rebuild_index():
    print("🔄 Rebuilding index...")

    # ---------------- PRODUCTS ----------------
    if DATA.get("products") is not None:
        df = DATA["products"]
        texts = pd.Series([""] * len(df))
        if "description" in df.columns:
            texts += df["description"].fillna("")
        if "name" in df.columns:
            texts += " " + df["name"].fillna("")
        if "category" in df.columns:
            texts += " " + df["category"].fillna("")
        INDEX["product_embeddings"] = model.encode(texts.tolist(), convert_to_numpy=True)
    else:
        INDEX["product_embeddings"] = None

    # ---------------- OFFERS ----------------
    if DATA.get("offers") is not None:
        df = DATA["offers"]
        texts = pd.Series([""] * len(df))
        if "title" in df.columns:
            texts += df["title"].fillna("")
        if "description" in df.columns:
            texts += " " + df["description"].fillna("")
        INDEX["offer_embeddings"] = model.encode(texts.tolist(), convert_to_numpy=True)
    else:
        INDEX["offer_embeddings"] = None

    # ---------------- CUSTOMERS ----------------
    if DATA.get("customers") is not None:
        df = DATA["customers"]
        id_col = "id" if "id" in df.columns else df.columns[0]

        # Use 'name' column (or first text column) to create numeric embeddings
        text_col = "name" if "name" in df.columns else df.columns[1] if len(df.columns) > 1 else df.columns[0]
        texts = df[text_col].fillna("").tolist()
        embeddings = model.encode(texts, convert_to_numpy=True)

        # Store numeric embeddings for each customer
        INDEX["customer_profiles"] = {
            str(row[id_col]): embeddings[i] for i, row in df.iterrows()
        }
    else:
        INDEX["customer_profiles"] = None

    print("✅ Indexing complete!")
