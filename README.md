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

## 🚀 How to Run the Project

### 1. Open the Project in VS Code
Make sure you open the correct folder:
```
C:\Users\meesh\projects\Midterm
```

### 2. Open a Terminal in VS Code
Go to:
```
Terminal → New Terminal
```

You should see something like:
```
PS C:\Users\meesh\projects\Midterm>
```

### 3. Activate the Environment
```bash
conda activate traffic_dashboard
```

### 4. Generate Fake Data
```bash
python generate_data.py
```

This creates the dataset used by the API and dashboard.

### 5. Start the API (Keep This Running)
```bash
uvicorn api:app --reload
```

You should see:
```
Uvicorn running on http://127.0.0.1:8000
```
⚠️ Do NOT close this terminal.
---

### 6. Open a New Terminal
Click the **+** button in the terminal panel, then run:
```bash
conda activate traffic_dashboard
python run_app.py
```

### 7. Open the Dashboard
Go to:
```
http://localhost:8501
```

## 🧠 How the System Works

This project is structured as a modular pipeline:

- **Data Layer**
  - `generate_data.py` → Creates synthetic congestion data

- **API Layer**
  - `api.py` → Serves data via endpoints:
    - `/congestion/current`
    - `/congestion/time`

- **AI Layer**
  - `ai_summary.py` → Generates natural language insights

- **Frontend Layer**
  - `app.py` → Dashboard interface

## ⚠️ Common Issues & Fixes

### Terminal Already Running
Use **two terminals**:
- Terminal 1 → API
- Terminal 2 → Dashboard

### Module Not Found Error
```bash
pip install -r requirements.txt
```

### API Not Working
Test in browser:
```
http://127.0.0.1:8000/congestion/current
```

### Dashboard Shows "No Data"
- Make sure you ran:
  ```bash
  python generate_data.py
  ```
- Ensure the API is running

## 💡 Why This Project Stands Out

- Real-time congestion insights  
- Historical trend comparison  
- AI-generated summaries  
- Modular system design (data → API → AI → UI)  

## 🔮 Future Improvements

- Add more locations and longer time ranges  
- Compare real-time vs historical averages automatically  
- Deploy to cloud (DigitalOcean / Posit Connect)  
