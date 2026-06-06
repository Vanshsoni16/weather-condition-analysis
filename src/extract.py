import zipfile

with zipfile.ZipFile("data/weather-dataset.zip", "r") as zip_ref:
    zip_ref.extractall("data")

print("Dataset extracted")