from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel


VERSION_FILE = Path(__file__).parent / "VERSION"

VERSION = VERSION_FILE.read_text().strip()


app = FastAPI(
    title="student-ml-api",
    version=VERSION
)


class PredictionRequest(BaseModel):
    value: float


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "application": "student-ml-api",
        "version": VERSION
    }


@app.post("/predict")
def predict(request: PredictionRequest):
    return {
        "input": request.value,
        "prediction": request.value * 2
    }