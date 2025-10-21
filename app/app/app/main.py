from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI(title="Data Lighthouse")

# Example data validation schema
class SalesData(BaseModel):
    item: str
    price: float
    quantity: int

@app.get("/")
def home():
    return {"message": "Welcome to Data Lighthouse API!"}

@app.post("/validate")
def validate_data(data: list[SalesData]):
    # Convert to DataFrame
    df = pd.DataFrame([d.dict() for d in data])

    # Check for missing or invalid values
    issues = {}
    if df.isnull().values.any():
        issues["missing_values"] = df.isnull().sum().to_dict()

    if (df["price"] <= 0).any():
        issues["invalid_prices"] = df[df["price"] <= 0].to_dict(orient="records")

    if issues:
        return {"status": "validation_failed", "issues": issues}
    else:
        return {"status": "success", "validated_data": df.to_dict(orient="records")}
