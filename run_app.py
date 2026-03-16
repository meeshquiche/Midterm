from dotenv import load_dotenv
import os

load_dotenv()  # must happen before importing ai_summary
print("API key loaded:", os.getenv("OPENAI_API_KEY")[:5] + "...")

# Now import the rest
from shiny import App, ui, render
import pandas as pd
import requests
from ai_summary import generate_summary
import webbrowser

from app import app

webbrowser.open("http://127.0.0.1:5000")
app.run(port=5000)