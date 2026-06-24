from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("placement_predictor.pkl")

class StudentData(BaseModel):
    gender: int
    age: int
    tenth_percentage: float
    twelfth_percentage: float
    degree_percentage: float
    internships_count: int
    projects_count: int
    city_tier: str
    degree_field: str

@app.get("/")
def home():
    return {
        "message": "Student Placement Predictor API"
    }

@app.post("/predict")
def predict(data: StudentData):

    input_df = pd.DataFrame([{
        "gender": data.gender,
        "age": data.age,
        "tenth_percentage": data.tenth_percentage,
        "twelfth_percentage": data.twelfth_percentage,
        "degree_percentage": data.degree_percentage,
        "internships_count": data.internships_count,
        "projects_count": data.projects_count,
        "city_tier": data.city_tier,
        "degree_field": data.degree_field
    }])

    prediction = model.predict(input_df)

    result = "Placed" if prediction[0] == 1 else "Not Placed"

    return {
        "prediction": result
    }