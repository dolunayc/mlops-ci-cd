from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI(title="MLOps CI/CD Service")


def hash_to_bucket(text: str, num_buckets: int = 100) -> int:
    h = 0
    for ch in text:
        h = (h * 31 + ord(ch)) % 1000000007
    return h % num_buckets


class PredictRequest(BaseModel):
    user_id: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict")
def predict(req: PredictRequest):
    bucket = hash_to_bucket(req.user_id, 100)
    return {"user_id": req.user_id, "bucket": bucket}
