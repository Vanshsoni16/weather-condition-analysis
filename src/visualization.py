import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/weather_clean.csv")

# Temperature Trend
plt.figure(figsize=(12,5))

plt.plot(df["Temperature (C)"])

plt.title("Temperature Trend")

plt.xlabel("Records")
plt.ylabel("Temperature (C)")

plt.savefig(
    "reports/temperature_trend.png"
)

plt.close()

# Humidity Histogram
plt.figure(figsize=(10,5))

plt.hist(df["Humidity"], bins=20)

plt.title("Humidity Distribution")

plt.savefig(
    "reports/humidity_distribution.png"
)

plt.close()

print("Graphs Saved")