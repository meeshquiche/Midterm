from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_csv("congestion_data.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"])

@app.get("/")
def home():
    return {"message": "Traffic Congestion API"}

@app.get("/congestion/high")
def high_congestion(threshold: int = 70):
    results = df[df["congestion_level"] > threshold]
    return results.to_dict(orient="records")

@app.get("/congestion/time")
def congestion_by_time(start: str, end: str):
    start_dt = pd.to_datetime(start)
    end_dt = pd.to_datetime(end)
    filtered = df[(df["timestamp"] >= start_dt) & (df["timestamp"] <= end_dt)]
    return filtered.to_dict(orient="records")

@app.get("/congestion/current")
def current():
    latest_time = df["timestamp"].max()
    current_data = df[df["timestamp"] == latest_time]
    return current_data.to_dict(orient="records")