import pandas as pd
import random
from datetime import datetime, timedelta

locations = [1,2,3,4,5]
rows = []

start = datetime(2026,3,1)

for day in range(14):
    for hour in range(24):
        for loc in locations:
            timestamp = start + timedelta(days=day, hours=hour)

            base = random.randint(20,60)

            if hour in [7,8,9,16,17,18]:
                base += random.randint(20,40)

            congestion = min(base,100)

            rows.append({
                "location_id": loc,
                "timestamp": timestamp,
                "congestion_level": congestion
            })

df = pd.DataFrame(rows)
df.to_csv("congestion_data.csv", index=False)