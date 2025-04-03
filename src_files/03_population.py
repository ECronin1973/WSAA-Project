import requests
import pandas as pd
import os

# API endpoint URL
url = "https://ws.cso.ie/public/api.jsonrpc"

# POST request payload
payload = {
    "jsonrpc": "2.0",
    "method": "PxStat.Data.Cube_API.ReadDataset",
    "params": {
        "class": "query",
        "id": ["TLIST(A1)", "C02076V02508", "C02199V02655"],
        "dimension": {
            "TLIST(A1)": {"category": {"index": ["2024", "2023", "2022", "2021", "2020"]}},
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

# Send POST request to the API
response = requests.post(url, json=payload)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()  # Parse JSON-stat response
    print("Population data retrieved successfully!")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    exit()

# Parse and structure data
values = data["result"]["value"]  # Population values
years = data["result"]["dimension"]["TLIST(A1)"]["category"]["label"]  # Year labels

# Combine data into a DataFrame
df = pd.DataFrame({"Year": list(years.values()), "Population (Thousand)": values})

# Save to a CSV file
output_dir = os.path.join(os.path.dirname(__file__), "../data")  # Relative directory
output_file = os.path.join(output_dir, "population_breakdown.csv")
os.makedirs(output_dir, exist_ok=True)  # Ensure the directory exists

df.to_csv(output_file, index=False)
print(f"Population data successfully saved to {output_file}")
