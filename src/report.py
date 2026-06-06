import pandas as pd

df = pd.read_csv("data/weather_clean.csv")

report = f"""
WEATHER CONDITION ANALYSIS REPORT

Total Records:
{len(df)}

Average Temperature:
{df['Temperature (C)'].mean():.2f}

Highest Temperature:
{df['Temperature (C)'].max():.2f}

Lowest Temperature:
{df['Temperature (C)'].min():.2f}

Average Humidity:
{df['Humidity'].mean():.2f}

Average Wind Speed:
{df['Wind Speed (km/h)'].mean():.2f}

Most Common Weather:
{df['Summary'].mode()[0]}
"""

with open(
    "reports/weather_report.txt",
    "w"
) as file:
    file.write(report)

print("Report Generated")