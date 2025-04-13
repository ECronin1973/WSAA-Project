# 01_fatalities.py
# This script fetches road fatalities data from the CSO API and saves it to a CSV file.
# It uses the requests library to make an API call and the csv library to write the data to a file.
# Author: Edward Cronin (g00425645)

import requests
import csv
import os

# Define the API endpoint for fetching road fatalities data
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/ROA29/JSON-stat/1.0/en"

# Fetch data using a GET request
response = requests.get(url, headers={"Content-Type": "application/json"})

# Check if the API request was successful
if response.status_code == 200:
    data = response.json()  # Parse the JSON response
    print("Data retrieved successfully!")
else:
    print(f"Failed to fetch data. HTTP Status code: {response.status_code}")
    exit()  # Terminate the program if data fetch fails

# Extract fatalities data and corresponding months from the JSON-stat response
road_fatalities = data["dataset"]["value"]
month_labels = data["dataset"]["dimension"]["TLIST(M1)"]["category"]["label"]

# Combine the parsed data into a structured format (list of dictionaries)
formatted_data = [
    {"Month": month_labels[str(key)], "Fatalities": int(road_fatalities[idx])}
    for idx, key in enumerate(month_labels.keys())
]

# Define the directory and file path for saving the data
output_dir = os.path.join(os.path.dirname(__file__), "../data")
output_file = os.path.join(output_dir, "road_fatalities.csv")
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

# Save the structured data to a CSV file
with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Month", "Fatalities"])  # Write CSV header row
    for entry in formatted_data:
        writer.writerow([entry["Month"], entry["Fatalities"]])

print(f"Data successfully saved to {output_file}")
