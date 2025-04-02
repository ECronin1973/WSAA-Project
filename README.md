# Road Safety Analysis Project

## Overview

This project aims to analyze road deaths in Ireland over the past five years, assessing monthly trends to determine whether fatalities have increased or decreased. The program also investigates correlations between road safety campaigns and reductions in road deaths. Users can update or delete data via the API, ensuring a dynamic and user-friendly experience.

## Author

- Name: Edward Cronin
- Student ID: g00425645
- Email: g00425645@atu.ie

## Table of Contents

- [Overview](#overview)
- [Author](#author)
- [Features](#features)
- [Technical Stack](#technical-stack)
- [Implementation Steps](#implementation-steps)
- [Pre-Requisites](#prerequisites)
- [How to Download this Repository](#how-to-download-this-repository)
- [Code of Conduct](#code-of-conduct)
- [Dependencies](#dependencies)
- [Data Content Relevant To Task](#data-content-relevant-to-task)
- [Project Structure](#project-structure)
- [Notebooks](#notebooks)
- [Licence](#license)
- [References](#references)

## Features

- **Data Representation**: Handles data in CSV, XML, and JSON formats.
- **Data Analysis**: Identifies monthly trends in road fatalities over five years and visualizes them with charts.
- **API Integration**: Fetches and interacts with data from the Road Safety Authority of Ireland API.
- **CRUD Functionality**: Allows users to Create, Read, Update, and Delete data directly from the application.
- **Authentication**: Uses OAuth for secure access and data management.
- **Visualization**: Provides user-friendly charts for clear trend analysis.

## Technical Stack

1. **Backend**
   - RESTful API development with Flask.
   - Integration with the Road Safety Authority API for data retrieval and updates.
2. **Frontend**
   - Interactive web interface using jQuery and AJAX.
   - Hosted on a cloud platform
3. **Data Analysis**
   - Data manipulation and analysis with `pandas`.
   - Visualization with `matplotlib` or `seaborn`.
4. **Testing**
   - API testing with Postman or CURL.
5. **Authentication**
   - Secure access using OAuth. (To Be Explored Further!!)

## Implementation Steps

1. **Accessing the API**
   - Retrieve road safety data using HTTP methods (`GET`) via CURL or Postman.
   - Parse data from CSV, XML, or JSON formats for monthly analysis.

2. **Data Analysis**
   - Analyze road deaths for trends using Python libraries.
   - Generate charts and visualizations to highlight changes in road fatalities.

3. **Connecting Campaign Data**
   - Cross-reference road safety campaigns and initiatives for potential correlations.
   - Integrate campaign data into the analysis.

4. **Interactive CRUD Operations**
   - Enable users to update or delete data directly via the API.
   - Develop CRUD functionalities using Flask for the backend.

5. **Frontend Development**
   - Create a user-friendly web interface for data visualization.
   - Use jQuery and AJAX for seamless asynchronous data retrieval.

6. **Deployment**
   - Host the project on ? (To be determindes during project).

7. **Authentication**
   - Implement OAuth for secure and authenticated data access.

## Prerequisites

- **Languages**: Python, JavaScript, HTML, CSS.
- **Tools**: Postman, CURL, Git, Flask.
- **Libraries**: `pandas`, `numpy`, `matplotlib`, `seaborn`, jQuery, AJAX.

## How to Download this Repository

To download this repository, you can use the following command:

```bash
git clone https://github.com/ECronin1973/WSAA-Project
```

## Code of Conduct

Please read the CODE_OF_CONDUCT.md file for details on our code of conduct.

## Dependencies

The dependencies for this project are listed in the requirements.txt file.

## Data Content Relevant To Task
```bash
https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/ROA29/JSON-stat/1.0/en
```

## Project Structure

To Be Added

## Notebooks

To Be Added

## License

This project is licensed under the Apache License 2.0. See the LICENSE file for details.

# Part A:  Access the API and Fetch the Data

## Step 1: Retrieve Road Safety Data via CURL

### Purpose:
Retrieve structured road fatalities data in JSON-stat format from the API endpoint for analysis and visualization.

### Command Used:
To make the GET request via Command Prompt, the following CURL command was executed:

```bash
curl -X GET "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/ROA29/JSON-stat/1.0/en" -H "Content-Type: application/json"
```
This command fetched the data and displayed the results directly in the terminal.

### Reference:
[CURL Documentation](https://curl.se/)

## Step 2: Retrieve Data Using Postman

### Purpose:
Use Postman to interact with the API and retrieve road fatalities data in JSON-stat format for analysis and visualization.

### Command Used:
The following steps were executed in Postman:

- Opened Postman and created a new request.
- Selected the HTTP method as GET.
- Pasted the URL: https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/ROA29/JSON-stat/1.0/en.
- Set the Content-Type header to application/json.
- Sent the request and reviewed the JSON-stat response displayed in Postman.

### What the Command Did:
The GET request fetched structured data from the API endpoint. The response provided detailed road fatalities information, formatted as JSON-stat, which can be further processed for analysis.

### Why It Was Necessary:
This step was critical for verifying the API's functionality and ensuring the data was accessible in a structured format suitable for parsing and visualization.

### Reference:
[Postman Documentation](https://www.postman.com/)

## Step 3: Parse and Convert Data

### Purpose:
Process the retrieved JSON-stat data and convert it into a structured CSV format for monthly road fatalities analysis.

### Code Used:
The following Python code was implemented to parse the JSON-stat response, structure the data, and save it as a CSV file:
```bash
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
```
### What the Code Did:

- Parsed the JSON-stat data from the API to extract monthly road fatalities and their corresponding labels.
- Organized the data into a structured format with months and fatality counts.
- Saved the processed data into a CSV file (road_fatalities.csv) within a specified directory (../data).

### Why It Was Necessary:
Converting the data into a CSV format allows for easy analysis, visualization, and compatibility with tools such as spreadsheets or Python libraries like pandas

### Reference:
[Requests Library Documentation](https://requests.readthedocs.io/en/latest/).  
Provides details on how to make HTTP requests, handle responses, and parse JSON data in Python.

[Python CSV Module Documentation](https://docs.python.org/3/library/csv.html).
Explains how to read from and write to CSV files in Python, ensuring structured data storage.

[JSON-stat Format](https://json-stat.org/).
JSON-stat is a lightweight format designed for statistical data.

[OS Module in Python](https://docs.python.org/3/library/os.html).
Useful for handling file paths and creating directories dynamically in Python.

## Step 4: Monthly Trend Analysis

### Purpose:
Analyze the monthly road fatalities data by grouping it to identify patterns or trends. This step provides insights into variations over time and can serve as a basis for further statistical analysis or visualization.

### Code Used:
The following Python code loads, filters, and analyzes the data saved in the CSV file and saves the filtered results as a new CSV file for the specified years:

```bash
import pandas as pd
import os

# Construct the relative path to the CSV file
csv_file = os.path.join(os.path.dirname(__file__), "../data/road_fatalities.csv")

# Load data from CSV
df = pd.read_csv(csv_file)

# Split the "Month" column into "Year" and "Month" columns
df["Year"] = df["Month"].str.split(" ").str[0]  # Extract Year
df["Month"] = df["Month"].str.split(" ").str[1]  # Extract Month

# Filter the DataFrame to include only rows corresponding to years 2024 to 2020
filtered_years = ["2024", "2023", "2022", "2021", "2020"]
filtered_df = df[df["Year"].isin(filtered_years)]  # Filter for relevant years

# Save the filtered data to a new Excel sheet
output_file = os.path.join(os.path.dirname(__file__), "../data/five_yr_fatalities.csv")
filtered_df.to_csv(output_file, index=False)  # Write to CSV without the index column

print(f"Filtered data successfully saved to {output_file}")

```
### What the Code did:
- **Load CSV File:** Reads the road_fatalities.csv file into a pandas DataFrame for analysis.
- **Extract Year and Month:**  Splits the "Month" column into two parts: "Year" and "Month". The year and month are extracted using the str.split() method.
- **Filter Relevant Data:** Filters the DataFrame to include only rows corresponding to the years 2024 to 2020 by checking if the "Year" column values are in the specified range.
- **Save Filtered Data:** Saves the filtered data into a new CSV file titled five_yr_fatalities.csv. This new file is stored in the same directory as the original file, making it easy to locate and use for further analysis or sharing.

### Why It Was Necessary:
Filtering the data to focus on the years 2024 to 2020 narrows the scope to the most recent and relevant period for analysis. Saving the filtered results into a new file ensures a clear, reusable dataset that can be used for further analysis or visualization. This cleaned format simplifies the exploration of trends and patterns.

### Reference:
[Pandas Documentation](https://pandas.pydata.org/docs/).
For reading, manipulating, and exporting data in DataFrames.

[Python OS Module](https://docs.python.org/3/library/os.html).
For constructing paths dynamically and ensuring compatibility across operating systems.



## References
- [CURL Documentation](https://curl.se/)
- [JSON-stat Format](https://json-stat.org/)
- [OS Module in Python](https://docs.python.org/3/library/os.html)
- [Postman Documentation](https://www.postman.com/)
- [Python CSV Module Documentation](https://docs.python.org/3/library/csv.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Python OS Module](https://docs.python.org/3/library/os.html)
- [Requests Library Documentation](https://requests.readthedocs.io/en/latest/).
