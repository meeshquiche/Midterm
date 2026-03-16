import os
import pandas as pd

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

# Read API key
api_key = os.getenv("OPENAI_API_KEY")

# Initialize client if possible
if OPENAI_AVAILABLE and api_key:
    client = OpenAI(api_key=api_key)
else:
    client = None

def generate_summary(df: pd.DataFrame) -> str:
    """
    Generate AI summary of congestion data.
    Falls back gracefully if OpenAI API key or package is missing.
    """

    if df.empty:
        return "No congestion data available."

    avg = df["congestion_level"].mean()
    
    # Use location if available
    if "location" in df.columns:
        top_locations = df.sort_values("congestion_level", ascending=False).head(3)["location"].tolist()
    else:
        top_locations = df.sort_values("congestion_level", ascending=False).head(3)["location_id"].tolist()

    prompt = f"""
You are a city transportation analyst.

Average congestion level: {avg:.2f}

Top congested locations:
{top_locations}

Provide a short actionable summary.
"""

    # If OpenAI is available
    if client:
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"AI summary failed: {e}"
    else:
        # Fallback summary
        return f"AI summary not available. Average congestion: {avg:.2f}, Top locations: {top_locations}"