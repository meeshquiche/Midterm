from shiny import App, ui, render
import pandas as pd
import requests
from ai_summary import generate_summary
import webbrowser

# Import existing app
from app import app

# Open browser automatically
webbrowser.open("http://127.0.0.1:5000")

# Run the app
app.run(port=5000)