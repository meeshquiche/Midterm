# ------------------------------
# Load environment variables first
# ------------------------------
from dotenv import load_dotenv
import os

load_dotenv()  # must happen BEFORE importing ai_summary
print("Loaded API key:", os.getenv("OPENAI_API_KEY"))  # debug: shows your key

# ------------------------------
# Imports
# ------------------------------
import streamlit as st
import pandas as pd
import requests
from datetime import datetime, timedelta
from ai_summary import generate_summary