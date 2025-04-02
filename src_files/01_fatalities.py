import requests
import csv
import os

# API endpoint
url = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/ROA29/JSON-stat/1.0/en"

# Fetch data using GET request
response = requests.get(url, headers={"Content-Type": "application/json"})

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse JSON response
    print("Data retrieved successfully!")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    exit()

# Parse the JSON-stat response for road fatalities
values = data["dataset"]["value"]
months = data["dataset"]["dimension"]["TLIST(M1)"]["category"]["label"]

# Combine data into a structured format
formatted_data = []
for index, fatalities in enumerate(values):
    month = months[str(list(months.keys())[index])]
    formatted_data.append({"Month": month, "Fatalities": int(fatalities)})  # Convert to integer

# Save the structured data to a CSV file
output_dir = os.path.join(os.path.dirname(__file__), "../data")  # Relative directory
output_file = os.path.join(output_dir, "road_fatalities.csv")
os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists

with open(output_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Month", "Fatalities"])  # Header row
    for entry in formatted_data:
        writer.writerow([entry["Month"], entry["Fatalities"]])

print(f"Data successfully saved to {output_file}")
# The data is now saved in the CSV file, ready for further analysis or visualization.