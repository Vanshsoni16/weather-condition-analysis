import pandas as pd

df = pd.read_csv(r"C:\Users\vansh soni\WEATHER_1\data\weatherHistory.csv")

df = df.drop_duplicates()

df = df.ffill()

df.to_csv(
    "data/weather_clean.csv",
    index=False
)

print("Cleaning complete")