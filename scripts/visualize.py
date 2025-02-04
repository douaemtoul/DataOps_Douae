import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/data.csv")
df = df[['date', 'positive']].dropna()

df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')

plt.figure(figsize=(10, 5))
plt.plot(df['date'], df['positive'], label="Cas positifs", marker="o")
plt.xlabel("Date")
plt.ylabel("Nombre de cas positifs")
plt.title("Évolution des cas positifs")
plt.legend()
plt.grid(True)

plt.savefig("data/visualization.png")
print("✅ Graphique sauvegardé dans data/visualization.png")
