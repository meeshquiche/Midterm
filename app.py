# ------------------------------
# Load environment variables first
# ------------------------------
from dotenv import load_dotenv
import os
load_dotenv()

import streamlit as st
import pandas as pd
from ai_summary import generate_summary

st.title("Traffic Congestion Dashboard")

# ------------------------------
# Load congestion data
# ------------------------------
DATA_FILE = "congestion_data.csv"

if not os.path.exists(DATA_FILE):
    st.error(f"{DATA_FILE} not found. Run generate_data.py first.")
    st.stop()

df = pd.read_csv(DATA_FILE)
df["timestamp"] = pd.to_datetime(df["timestamp"])

st.write("### Data preview")
st.dataframe(df.head())

# ------------------------------
# Filters
# ------------------------------
st.sidebar.header("Filters")
locations = sorted(df["location_id"].unique())
selected_locations = st.sidebar.multiselect("Select Locations", locations, default=locations)

time_range = st.sidebar.date_input("Select Date Range",
                                   [df["timestamp"].min().date(), df["timestamp"].max().date()])

start_date = pd.to_datetime(time_range[0])
end_date = pd.to_datetime(time_range[1]) + pd.Timedelta(days=1) - pd.Timedelta(seconds=1)

filtered_df = df[
    (df["location_id"].isin(selected_locations)) &
    (df["timestamp"] >= start_date) &
    (df["timestamp"] <= end_date)
]

st.write(f"### Filtered Data ({len(filtered_df)} rows)")
st.dataframe(filtered_df)

# ------------------------------
# AI Summary
# ------------------------------
st.write("### AI Summary")
summary_text = generate_summary(filtered_df)
st.write(summary_text)