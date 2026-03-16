from openai import OpenAI
import pandas as pd

client = OpenAI()

def generate_summary(df):

    avg = df["congestion_level"].mean()

    top = df.sort_values("congestion_level", ascending=False).head(3)

    top_locations = top["location"].tolist()

    prompt = f"""
    You are a city transportation analyst.

    Average congestion level: {avg}

    Top congested locations:
    {top_locations}

    Provide a short actionable summary.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response.choices[0].message.content