from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from indexer import DATA, INDEX, rebuild_index
from recommender_full import get_recommendations_for_user
from fastapi.responses import FileResponse
import os

app = FastAPI()

# Allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_TRACKER = {key: False for key in DATA.keys()}

def check_and_auto_index():
    if all(UPLOAD_TRACKER.values()):
        print("🔥 All CSVs uploaded → Auto indexing now…")
        rebuild_index()
        print("🎉 Auto indexing completed!")

# ---------------- CSV Upload Endpoint ----------------
@app.post("/upload/{csv_type}")
async def upload_csv(csv_type: str, file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    if csv_type in DATA:
        DATA[csv_type] = df
        UPLOAD_TRACKER[csv_type] = True
        check_and_auto_index()
        return {"status": f"{csv_type} uploaded"}
    return {"status": "invalid csv type"}

# ---------------- Users Endpoint ----------------
@app.get("/users")
def get_users():
    df = DATA.get("customers", pd.DataFrame())
    if df.empty:
        return []

    id_col = "id" if "id" in df.columns else df.columns[0]
    name_col = "name" if "name" in df.columns else df.columns[1] if len(df.columns) > 1 else df.columns[0]

    return [{"id": row[id_col], "name": row.get(name_col, "")} for _, row in df.iterrows()]

# ---------------- Single User Recommendation ----------------
@app.get("/recommend/{user_id}")
def recommend(user_id: str):
    recs = get_recommendations_for_user(str(user_id))
    if recs is None:
        return {"error": "customer not found"}

    products, offers = recs
    return {
        "user_id": user_id,
        "products": products.to_dict(orient="records"),
        "offers": offers.to_dict(orient="records")
    }

# ---------------- Bulk Recommendations in Columns ----------------
@app.get("/bulk_recommend_columns")
def bulk_recommend_columns(top_n_products: int = 5, top_n_offers: int = 3):
    """
    Return all users' recommendations in separate columns for CSV/table display
    """
    if DATA.get("customers") is None:
        return []

    customers = DATA["customers"]
    id_col = "id" if "id" in customers.columns else customers.columns[0]

    result = []
    for _, row in customers.iterrows():
        user_id = str(row[id_col])
        recs = get_recommendations_for_user(user_id)
        if recs is None:
            continue

        products, offers = recs
        products_list = products.head(top_n_products)["name"].tolist() if "name" in products.columns else products.head(top_n_products).iloc[:,0].tolist()
        offers_list = offers.head(top_n_offers)["title"].tolist() if "title" in offers.columns else offers.head(top_n_offers).iloc[:,0].tolist()

        user_dict = {"user_id": user_id}
        for i, prod in enumerate(products_list, start=1):
            user_dict[f"product_{i}"] = prod
        for i, off in enumerate(offers_list, start=1):
            user_dict[f"offer_{i}"] = off

        result.append(user_dict)

    return result

# ---------------- Export Bulk Recommendations as CSV ----------------
@app.get("/export_csv")
def export_csv(top_n_products: int = 5, top_n_offers: int = 3):
    data = bulk_recommend_columns(top_n_products, top_n_offers)
    if not data:
        return {"status": "No recommendations available"}

    df = pd.DataFrame(data)
    file_path = "bulk_recommendations.csv"
    df.to_csv(file_path, index=False)
    return FileResponse(path=file_path, filename="bulk_recommendations.csv", media_type="text/csv")
