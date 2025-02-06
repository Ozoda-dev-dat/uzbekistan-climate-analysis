import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("uzbekistan_climate.csv")
print(df.head())
plt.figure(figsize=(10, 5))
sns.lineplot(x=df["Year"], y=df["AverageTemperature"], marker="o", color="red", linewidth=2.5)
plt.title("O‘zbekistonda O‘rtacha Haroratning O‘zgarishi (1900-2023)", fontsize=14)
plt.xlabel("Yil", fontsize=12)
plt.ylabel("O‘rtacha Harorat (°C)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.7)

plt.savefig("climate_trend.png")
plt.show()
