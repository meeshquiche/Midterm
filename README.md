# City Congestion Monitoring Dashboard for SYSEN 5381 Midterm

Hey! This is my midterm project for the DL Challenge 2026. It’s a small city dashboard that shows congestion levels in a city, lets you explore them over time, and even gives short AI-generated summaries of what’s going on.

---

## What this does

### Simulates congestion data
- 5 locations, 14 days, hourly readings.  
- Congestion is higher during morning and evening peaks.  
- Data is stored in a CSV (`congestion_data.csv`) — kind of like a mini database.

### REST API
- Built with **FastAPI** (`api.py`).  
- Endpoints:
  - `/` → simple “API is live” message  
  - `/congestion/high?threshold=70` → returns rows where congestion is above a threshold  
  - `/congestion/time?start=&end=` → returns rows between two timestamps  
  - `/congestion/current` → latest readings only  

### Dashboard App
- Built with **Streamlit / Python Shiny** (`app.py` + `run_app.py`).  
- Lets you pick locations, filter by time, and see tables of congestion data.  
- Shows a short AI summary of traffic patterns.  

### AI summary
- File: `ai_summary.py`  
- Generates average congestion, top congested locations, and actionable insights.  
- Works even if OpenAI API key is missing (fallback summary).  

---

## How to run it

1. Activate your environment:

```bash
conda activate traffic_dashboard
python generate_data.py
uvicorn api:app --reload
python run_app.py

## File Guide

| File | Purpose |
|------|---------|
| `generate_data.py` | Creates fake congestion data |
| `api.py` | REST API to access data |
| `ai_summary.py` | Generates AI-based summaries |
| `app.py` | Streamlit/Shiny dashboard |
| `run_app.py` | Launches the dashboard in your browser |
| `.env` | Stores OpenAI API key (ignored in GitHub) |

---

## Why this is cool

- You can see which locations are congested **right now**.  
- Compare current congestion to **recent trends**.  
- Get a **plain-language summary with AI**.  
- All components (**data → API → dashboard → AI**) talk to each other seamlessly.  

---

## Future Improvements

- Add more locations or longer time periods.  
- Compare today’s congestion vs historical averages automatically.  
- Deploy fully to **DigitalOcean or Posit Connect** so anyone can open it in a browser.  

---

## Testing

Run the dashboard locally and try these queries:

- “Which intersections are worst right now?” → `/congestion/current`  
- “Show me high congestion locations over the last 3 days” → `/congestion/time`  
- “Get AI summary of today’s traffic” → summary displayed in dashboard
