from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_csv("congestion_data.csv")

@app.get("/")
def home():
    return {"message": "Traffic Congestion API"}

@app.get("/congestion/high")
def high_congestion(threshold: int = 70):

    results = df[df["congestion_level"] > threshold]

    return results.to_dict(orient="records")

@app.get("/congestion/time")
def congestion_by_time(start: str, end: str):

    filtered = df[(df["timestamp"] >= start) & (df["timestamp"] <= end)]

    return filtered.to_dict(orient="records")

@app.get("/congestion/current")
def current():

    latest_time = df["timestamp"].max()

    current_data = df[df["timestamp"] == latest_time]

    return current_data.to_dict(orient="records")