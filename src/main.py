from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import pickle
import pandas as pd

from .data_model import Water 

app = FastAPI(
    title="Water Potability Prediction API",
    description="API for predicting water potability using a machine learning model.",
)

# Add CORS middleware to allow requests from any origin (for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://water-portability-front-4ry2j5r3l.vercel.app"],  # In production, specify your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

with open("model/model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.get("/")
def index():
    return {"message": "Welcome to the Water Potability Prediction API"}

@app.post("/predict")
def model_predict(water: Water):
    sample = pd.DataFrame({
        'ph' : [water.ph],
        'Hardness' : [water.Hardness],
        'Solids' :[water.Solids],
        'Chloramines' :[water.Chloramines],
        'Sulfate' : [water.Sulfate],
        'Conductivity' :[water.Conductivity],
        'Organic_carbon' :[water.Organic_carbon],
        'Trihalomethanes' : [water.Trihalomethanes],
        'Turbidity' :[water.Turbidity]
    })

    predicted_value = model.predict(sample)[0]
    
    if predicted_value == 1:
        result = "Potable"
    else:
        result = "Not Potable"
        
    return {"prediction": result}
