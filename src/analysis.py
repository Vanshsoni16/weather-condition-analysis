import pandas as pd

df = pd.read_csv("data/weather_clean.csv")

print("\nColumns:")
print(df.columns.tolist())

print("\nDataset Shape:")
print(df.shape)

print("\nSummary Statistics:")
print(df.describe())

print("\nWeather Types:")
print(df["Summary"].value_counts())

print("\nPrecipitation Types:")
print(df["Precip Type"].value_counts())

print("\nAverage Temperature:")
print(df["Temperature (C)"].mean())

print("\nHighest Temperature:")
print(df["Temperature (C)"].max())

print("\nLowest Temperature:")
print(df["Temperature (C)"].min())

print("\nAverage Humidity:")
print(df["Humidity"].mean())

print("\nAverage Wind Speed:")
print(df["Wind Speed (km/h)"].mean())
numeric = df.select_dtypes(include="number")

print("\nCorrelation Matrix")

print(numeric.corr())