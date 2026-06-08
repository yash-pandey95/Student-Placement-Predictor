from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()

model = joblib.load("placement_predictor.pkl")

class StudentData(BaseModel):
    ssc_percentage: float
    hsc_percentage: float
    degree_percentage: float
    internships_count: int
    projects_count: int

@app.get("/")
def home():
    return {"message": "Student Placement Predictor API"}

@app.post("/predict")
def predict(data: StudentData):
    return {"received_data": data}


feature_names = joblib.load("feature_names.pkl")

@app.get("/features")
def features():
    return {
        "total_features": len(feature_names),
        "features": feature_names
    }

@app.get("/model-info")
def model_info():
    return {
        "model_type": str(type(model)),
        "features_required": 29
    }