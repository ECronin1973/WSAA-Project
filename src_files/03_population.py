# 03_population.py
# This script fetches population data from the CSO API and saves it to a CSV file.
# It uses the requests library to make an API call and pandas to handle data manipulation.
# Author: Edward Cronin (g00425645)

import requests
import pandas as pd
import os

# Define the API endpoint URL for fetching population data
url = "https://ws.cso.ie/public/api.jsonrpc"

# Construct POST request payload
current_year = 2024  # Replace this with dynamic calculation if needed
year_range = [str(year) for year in range(current_year, current_year - 5, -1)]  # Last 5 years dynamically

payload = {
    "jsonrpc": "2.0",
    "method": "PxStat.Data.Cube_API.ReadDataset",
    "params": {
        "class": "query",
        "id": ["TLIST(A1)", "C02076V02508", "C02199V02655"],
        "dimension": {
            "TLIST(A1)": {"category": {"index": year_range}},
            "C02076V02508": {"category": {"index": ["-"]}},
            "C02199V02655": {"category": {"index": ["-"]}},
        },
        "extension": {
            "pivot": None,
            "codes": False,
            "language": {"code": "en"},
            "format": {"type": "JSON-stat", "version": "2.0"},
            "matrix": "PEA01"
        },
        "version": "2.0"
    }
}

try:
    # Send POST request to the API
    response = requests.post(url, json=payload)
    response.raise_for_status()  # Check for HTTP request errors
    data = response.json()  # Parse JSON-stat response
    print("Population data retrieved successfully!")
except requests.exceptions.RequestException as e:
    print(f"Error while fetching data: {e}")
    exit()
except KeyError:
    print("Unexpected data structure in JSON response.")
    exit()

# Extract population values and corresponding year labels
try:
    population_values = data["result"]["value"]  # Population values
    year_labels = data["result"]["dimension"]["TLIST(A1)"]["category"]["label"]  # Year labels
except KeyError:
    print("Failed to extract necessary data from the JSON response.")
    exit()

# Combine the extracted data into a DataFrame
population_data = pd.DataFrame({
    "Year": list(year_labels.values()),
    "Population (Thousand)": population_values
})

# Define the output directory and file path for saving the data
output_dir = os.path.join(os.path.dirname(__file__), "../data")
output_file = os.path.join(output_dir, "population_breakdown.csv")
os.makedirs(output_dir, exist_ok=True)  # Create directory if it doesn't exist

try:
    # Save the DataFrame to a CSV file
    population_data.to_csv(output_file, index=False)
    print(f"Population data successfully saved to {output_file}")
except Exception as e:
    print(f"An error occurred while writing the file: {e}")
    exit()
