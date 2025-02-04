import pandas as pd
import requests

API_URL = "https://api.covidtracking.com/v1/states/daily.json"

response = requests.get(API_URL)
data = response.json()

df = pd.DataFrame(data)
df.to_csv("data/data.csv", index=False)

print("✅ Données téléchargées dans data/data.csv")
