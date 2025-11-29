from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import chromadb
import uvicorn
import json, os, requests
import pandas as pd

# ---------------------------
# App Initialization
# ---------------------------
app = FastAPI(title="Clothing Brand Recommender")

# CORS (allow requests from anywhere)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ---------------------------
# ChromaDB Setup
# ---------------------------
CHROMA_DIR = os.getenv("CHROMA_DIR", "./chroma_db")
client = chromadb.PersistentClient(path=CHROMA_DIR)
collection = client.get_or_create_collection("marketing_data")

# ---------------------------
# Ollama Settings
# ---------------------------
OLLAMA_URL = os.getenv("OLLAMA_URL", "http://localhost:11434/api/generate")
MODEL_NAME = os.getenv("MODEL_NAME", "llama3")

class Query(BaseModel):
    user_query: str

# ---------------------------
# CSV UPLOAD + INDEXING
# ---------------------------
@app.post("/upload_csv/")
async def upload_csv(file: UploadFile = File(...), type_name: str = "data"):
    """
    Upload a CSV and index it in ChromaDB.
    type_name: products / purchases / reviews
    """
    contents = await file.read()
    df = pd.read_csv(pd.io.common.BytesIO(contents))

    docs, ids = [], []

    for i, row in df.iterrows():
        docs.append(f"{type_name} | {row.to_dict()}")
        ids.append(f"{type_name}_{i}")

    collection.add(documents=docs, ids=ids)

    return {"status": "indexed", "rows": len(df), "type": type_name}

# ---------------------------
# Helper: Call Ollama (streaming)
# ---------------------------
def call_ollama(prompt: str):
    try:
        payload = {
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": True
        }
        resp = requests.post(OLLAMA_URL, json=payload, stream=True, timeout=90)
        resp.raise_for_status()

        output = []
        for line in resp.iter_lines():
            if not line:
                continue
            try:
                obj = json.loads(line.decode("utf-8"))
                if "response" in obj:
                    output.append(obj["response"])
            except:
                continue

        return "".join(output)

    except Exception as e:
        return f"ERROR calling Ollama: {e}"

# ---------------------------
# Recommend Endpoint
# ---------------------------
@app.post("/recommend/")
async def recommend(q: Query):
    """
    Generate personalized clothing recommendations for a user.
    """
    try:
        res = collection.query(query_texts=[q.user_query], n_results=6)
        docs = res.get("documents", [[]])[0]
    except Exception as e:
        return {"result": f"Vector DB error: {e}", "matches": []}

    context = "\n".join(docs)

    prompt = f"""
You are a personalized product recommendation assistant for a clothing brand.

Use ONLY the context below to generate recommendations.

Provide:
1) Top 3 personalized clothing product recommendations for the user
2) 2 cross-sell / upsell clothing suggestions
3) A 1-line marketing message per product
4) A recommendation score (0-100)
5) Return results in clean bullet points

Context:
{context}

Query:
{q.user_query}
"""

    llm_output = call_ollama(prompt)

    return {
        "result": llm_output,
        "matches": docs
    }

# ---------------------------
# Run server
# ---------------------------
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
