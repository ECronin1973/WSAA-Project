# Road Safety Analysis Project

## Overview

The Road Safety Analysis Project examines road fatalities in Ireland over the past five years, identifying trends and patterns in fatality rates. The project integrates data from the Central Statistics Office (CSO) API and provides a custom API for CRUD operations on locally stored data. It also includes data visualization and analysis tools to offer insights into road safety trends. The project is designed to be user-friendly, secure, and extensible.

### Key Features:
- **Data Integration**: Fetches road safety data from the CSO API and processes it for analysis.
- **Custom API**: Implements a Flask-based API to enable CRUD operations on locally stored data.
- **Data Analysis**: Analyzes trends in road fatalities and visualizes them using charts.
- **Frontend Interface**: Provides an interactive web interface for data visualization and management.
- **Secure Access**: Incorporates OAuth for secure data access (future scope).

## Author

- **Name**: Edward Cronin
- **Student ID**: g00425645
- **Email**: g00425645@atu.ie

## Table of Contents

- [Overview](#overview)
- [Author](#author)
- [Features](#features)
- [Technical Stack](#technical-stack)
- [Implementation Steps](#implementation-steps)
- [Pre-Requisites](#pre-requisites)
- [How to Download this Repository](#how-to-download-this-repository)
- [Code of Conduct](#code-of-conduct)
- [Dependencies](#dependencies)
- [Data Content Relevant To Task](#data-content-relevant-to-task)
- [Project Structure](#project-structure)
- [License](#license)
- [Part A: Access the API's and Fetch the Data](#part-a-access-the-api's-and-fetch-the-data)
- [Part B: Analysis](#part-b-analysis)
- [Part C: CRUD API](#part-c-crud-api)
- [Part D: Front End Development](#front-end-development)
- [Part E: OAuth (Open Authorization)](#Oauth-open-authorization)
- [Project References](#Project-References)

## Features

- **Data Representation**: Handles data in CSV, XML, and JSON formats.
- **Data Analysis**: Identifies monthly trends in road fatalities and visualizes them with charts.
- **Custom API**: Enables CRUD operations on locally stored data using Flask.
- **Frontend Interface**: Provides a web-based interface for data visualization and management.
- **Authentication**: Implements OAuth for secure access (future scope).

## Technical Stack

1. **Backend**:
   - Flask for RESTful API development.
   - Integration with the CSO API for data retrieval.
2. **Frontend**:
   - Interactive web interface using HTML, CSS, jQuery, and AJAX.
3. **Data Analysis**:
   - Data manipulation and visualization using `pandas`, `matplotlib`, and `seaborn`.
4. **Testing**:
   - API testing with Postman and CURL.
5. **Authentication**:
   - OAuth for secure access (future scope).

## Implementation Steps

1. **Data Retrieval**:
   - Fetch road safety data from the CSO API using HTTP GET requests.
   - Parse and convert the data into CSV format for analysis.
2. **Data Analysis**:
   - Analyze trends in road fatalities using Python libraries.
   - Visualize data with charts and graphs.
   - Analyse yearly fatality totals per capita and per 100,000 population.
3. **Custom API Development**:
   - Implement a Flask-based API to enable CRUD operations on the locally stored data.
4. **Frontend Development**:
   - Create a web interface for data visualization and management.
   - Use AJAX for seamless data retrieval and updates.
5. **Authentication**:
   - Explore OAuth for secure access to the API (future scope).

## Pre-Requisites

- **Languages**: Python, JavaScript, HTML, CSS.
- **Tools**: Postman, CURL, Git, Flask.
- **Libraries**: `pandas`, `numpy`, `matplotlib`, `seaborn`, jQuery, AJAX.

## How to Download this Repository

To download this repository, use the following command:

```bash
git clone https://github.com/ECronin1973/WSAA-Project
```

## Code of Conduct

Please read the CODE_OF_CONDUCT.md file for details on our code of conduct.

## Dependencies

The dependencies for this project are listed in the `requirements.txt` file.

## Data Content Relevant To Task

- [CSO Website - STATS API](https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/ROA29/JSON-stat/1.0/en)

## Project Structure

The project is organized as follows:

```plaintext
WSAA-Project/
│
├── data/
│   ├── fatalities_data.png                                 # Visualization of road fatalities data
│   ├── Fatalities_per_1000.png                             # Fatalities per 100,000 population graph
│   ├── fatalities_trend_graph.png                          # Visualization of trends
│   ├── fatality_analysis_chart.png                         # Dual-axis chart for fatalities analysis
│   ├── fatality_analysis.csv                               # Yearly fatalities analysis results
│   ├── fatality_trends.csv                                 # Trend analysis results
│   ├── five_yr_fatalities.csv                              # Filtered road fatalities data
│   ├── monthly_fatalities_over_the_last_5_years.png        # Monthly fatalities graph
│   ├── population_breakdown.csv                            # Population data from CSO API
│   ├── road_fatalities.csv                                 # Processed road fatalities data
│   ├── terminal_message_crud_api.png                       # Terminal output for CRUD API   
│   └── terminal_output_fatalities_per_capita.png          # Terminal output for fatalities per capita
│
├── src_files/
│   ├── 01_fatalities.py                                    # Script to fetch data from CSO API
│   ├── 02_trendanalysis.py                                 # Script for trend analysis
│   ├── 03_population.py                                    # Script to fetch population data from CSO API
│   ├── 04_data_analysis.py                                 # Script for data analysis and visualization
│   ├── 05_app.py                                           # Flask API for CRUD operations
│   └── 06_analyze_fatalities.py                           # Script for analyzing fatalities per capita
│
├── static/
│   ├── index.html                   # Frontend HTML file
│   ├── app.js                       # Frontend JavaScript file
│   └── styles.css                   # Frontend CSS file
│
├── README.md                        # Project documentation
├── requirements.txt                 # Python dependencies
└── LICENSE                          # License file
```

## License

This project is licensed under the Apache License 2.0. See the LICENSE file for details.

# Part A:  Access the API's and Fetch the Data

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

## Step 5 Retrieve population data from the CSO API 
Retrieve population data from the CSO API in JSON-stat format, parse the data, and export it to an Excel sheet for visualization and analysis

### Code Used:
The following Python code was implemented to parse the JSON-stat response, structure the data, and save it as a CSV file:

```bash
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
```

### What the Code did:
- **Retrieves Data:** Uses a POST request to interact with the CSO API and fetch population data for the years 2020–2024.
- **Structures Data:** Parses the JSON-stat response, organizes the population data alongside year labels, and stores them in a pandas DataFrame.
- **Exports Data:** Writes the DataFrame into an Excel file (population_breakdown.csv) within the ../data directory for convenient storage and usage.

### Why is it necessary:
Converting population data into a structured CSV format ensures compatibility with a wide range of analytical tools and platforms, such as Python, Excel, or data visualization software.

### Reference
- [Requests Library Documentation](https://requests.readthedocs.io/en/latest/)
- [Pandas Documentation](https://pandas.pydata.org/)
- [JSON-stat Format](https://json-stat.org/)

## PART B : Analysis 

### Part One : Road Fatalities Analysis

### Purpose:
The purpose of this analysis is to examine road fatalities over the last five years, identify trends, and visualize the data. The analysis includes detecting increases or decreases in fatalities, splitting the data into quarters for better insights, and saving the results for further use. The results are presented in a line graph with quarterly splits and saved as a CSV file for trend analysis.

![Fatalities_trend_graph.png](./data/fatalities_trend_graph.png)

### Code Used:

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load the data
csv_file = os.path.join(os.path.dirname(__file__), "../data/five_yr_fatalities.csv")
df = pd.read_csv(csv_file)

# Group data by Year and Month to calculate total fatalities
df_grouped = df.groupby(["Year", "Month"], as_index=False).sum()

# Sort the data by Year and Month for proper visualization
month_order = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
df_grouped["Month"] = pd.Categorical(df_grouped["Month"], categories=month_order, ordered=True)
df_grouped = df_grouped.sort_values(by=["Year", "Month"])

# Detect increases or decreases in fatalities
df_grouped["Change"] = df_grouped["Fatalities"].diff().fillna(0)  # Calculate the difference between consecutive rows
df_grouped["Trend"] = df_grouped["Change"].apply(lambda x: "Increase" if x > 0 else "Decrease" if x < 0 else "No Change")

# Save the trend data to a CSV file
trend_data_file = os.path.join(os.path.dirname(__file__), "../data/fatality_trends.csv")
df_grouped.to_csv(trend_data_file, index=False)
print(f"Trend data saved to {trend_data_file}")

# Visualization: Line plot for fatalities over time with quarterly splits
plt.figure(figsize=(12, 6))
sns.lineplot(data=df_grouped, x="Month", y="Fatalities", hue="Year", marker="o")

# Add vertical lines to split quarters
quarter_splits = ["March", "June", "September"]
for quarter in quarter_splits:
    plt.axvline(x=quarter, color="red", linestyle="--", alpha=0.7)

# Annotate quarters
plt.text(1.5, df_grouped["Fatalities"].max() + 2, "Q1", ha="center", fontsize=10, color="black")
plt.text(4.5, df_grouped["Fatalities"].max() + 2, "Q2", ha="center", fontsize=10, color="black")
plt.text(7.5, df_grouped["Fatalities"].max() + 2, "Q3", ha="center", fontsize=10, color="black")
plt.text(10.5, df_grouped["Fatalities"].max() + 2, "Q4", ha="center", fontsize=10, color="black")

# Add labels to the points (totals over each value)
for i, row in df_grouped.iterrows():
    plt.text(row["Month"], row["Fatalities"] + 0.5, str(row["Fatalities"]), ha="center", fontsize=8)

# Chart details
plt.title("Monthly Road Fatalities Over the Last 5 Years with Quarterly Splits")
plt.xlabel("Month")
plt.ylabel("Fatalities")
plt.legend(title="Year")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the graph to the data folder
graph_file = os.path.join(os.path.dirname(__file__), "../data/fatalities_trend_graph.png")
plt.savefig(graph_file)
print(f"Graph saved to {graph_file}")

plt.show()
```

### What the Code Did:

1. **Load Data**:
   - The code reads the `five_yr_fatalities.csv` file, which contains monthly road fatalities data for the last five years.

2. **Group and Sort Data**:
   - Groups the data by `Year` and `Month` to calculate total fatalities for each month.
   - Sorts the months in calendar order for proper visualization.

3. **Detect Trends**:
   - Calculates the change in fatalities between consecutive months.
   - Categorizes the trend as "Increase," "Decrease," or "No Change."

4. **Save Trend Data**:
   - Saves the grouped and processed data, including the trend information, to a CSV file named fatality_trends.csv.

5. **Visualize Data**:
   - Creates a line graph showing monthly fatalities for each year.
   - Adds vertical dashed lines to split the graph into quarters (Q1, Q2, Q3, Q4).
   - Annotates the quarters and adds labels above each data point to display the exact fatality totals.

6. **Save Graph**:
   - Saves the graph as an image file (`fatalities_trend_graph.png`) in the `data` folder.

### Output:

#### 1. **Trend Data (`fatality_trends.csv`)**:
The trend data includes the following columns:
- `Year`: The year of the data.
- `Month`: The month of the data.
- `Fatalities`: The total fatalities for the month.
- `Change`: The difference in fatalities compared to the previous month.
- `Trend`: Indicates whether the fatalities increased, decreased, or remained the same.

Example:
```csv
Year,Month,Fatalities,Change,Trend
2020,January,9,0.0,No Change
2020,February,19,10.0,Increase
2020,March,17,-2.0,Decrease
...
```

#### 2. **Graph (`fatalities_trend_graph.png`)**:
- A line graph showing monthly fatalities for each year.
- Vertical dashed lines split the graph into quarters (Q1, Q2, Q3, Q4).
- Labels above each data point display the exact fatality totals.

### Why It Was Necessary:
- **Trend Analysis**: Helps identify patterns in road fatalities over time, such as seasonal trends or sudden spikes.
- **Quarterly Insights**: Splitting the data into quarters provides a clearer understanding of how fatalities vary throughout the year.
- **Data Storage**: Saving the trend data and graph ensures the results are reusable for further analysis or reporting.

### References:
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Seaborn Documentation](https://seaborn.pydata.org/)
- [Python OS Module](https://docs.python.org/3/library/os.html)

### Summary of Analysis

- **Steady Decrease in Early 2021:** The first quarter (January-March) of 2021 showed a significant drop in fatalities, starting at 3 in January, then climbing slightly by March. This reflects a potential stabilization.
- **Highest Single-Year Increase:** December 2021 saw the highest single-month increase in fatalities (+16).
- **Consistent Seasonal Declines:** Across all years, October-December consistently experienced decreases in fatalities.
- **Notable Decline in Early 2023:** January to March 2023 showed a consistent decrease in fatalities, ending March at only 11 fatalities.
- **Rise in August Each Year:** August generally experienced increases in fatalities across most years, notably in 2021 (+4), 2023 (+9), and 2020 (+6).
- **Volatility in June:** June saw fluctuating trends year-on-year, ranging from increases in 2021 (+2) to sharp decreases in 2023 (-10).
- **Overall Decrease in 2022:** Year 2022 exhibited more months of decreasing fatalities compared to prior years, indicating a calmer trend overall.
- **Spike in May 2023:** A sharp increase was recorded in May 2023, with fatalities reaching 20 (+10).
- **Decreasing Trends in Q4:** Quarter 4 (October-December) consistently exhibited declining trends in fatalities, highlighting seasonal patterns.
- **Recurring Stability in September:** Several Septembers showed minimal change or minor decreases, suggesting consistency.

### Quarterly Summary:

**January to March:**
- 2020: Fatalities fluctuated from 9 to 17.
- 2021: Dropped to as low as 3, then slowly rebounded to 9.
- 2022: Stable increase from 13 to 16.
- 2023: Decline from 16 to 11.
- 2024: Minor fluctuations, ending at 18 fatalities in March.

**April to June:**
- 2020: Fatalities reduced sharply, hitting a low of 6 in May, then rose in June.
- 2021: Spiked sharply to 18 in April, then fluctuated.
- 2022: Gradual increase, peaking at 13 in June.
- 2023: Fatalities sharply declined in June (-10).
- 2024: Fluctuated minimally, reaching 11 in June.

**July to September:**
- 2020: Steady increases by September to 17.
- 2021: Volatility peaked at 21 in August, before dipping sharply in September.
- 2022: Relatively stable trend, reducing to 9 in September.
- 2023: Extreme fluctuation, from 26 in August to 9 in September.
- 2024: Stable trends with minor changes, staying within 12-21 fatalities.

**October to December:**
- 2020: Declined consistently, ending at 8 fatalities.
- 2021: Volatile, peaking at 19 in December.
- 2022: Saw mixed trends, ending with a decline.
- 2023: Significant spike to 22 in October, followed by a stabilization.
- 2024: Fluctuating trend, peaking at 17 in November

### Part Two : Analyse yearly fatality totals per capita and per 100,000 population

### Tasks performed by the code:

The code performs the following tasks:

**Load Data:** Reads road fatalities and population data from CSV files into pandas DataFrames.

**Calculate Yearly Fatalities:** Groups the fatalities data by year and calculates the total fatalities for each year.

**Merge Data:** Combines the yearly fatalities data with the population data based on the year.
Merge Data: Combines the yearly fatalities data with the population data based on the year.

**Calculate Metrics:** Computes two key metrics:
  - Fatalities per Capita: Calculates fatalities as a proportion of the total population.
  - Fatalities per 100,000 Population: Normalizes fatalities to a standard scale for easier comparison across years.

**Output Results:** Displays the merged data, including the calculated metrics, in the console and saves it to a new CSV file (fatality_analysis.csv).

**Visualize Data:** Creates visualizations:
  - A line chart titled 'Fatalities_per_1000.png' displaying fatalities per 100,000 population over the years.
  ![Fatalities_per_1000.png](./data/Fatalities_per_1000.png)
  - A dual-axis chart titled 'fatality_analysis_chart.png' combining the bar chart (total fatalities) and line chart (fatalities per 100,000) for a comprehensive view.
  ![fatality_analysis_chart.png](./data/fatality_analysis_chart.png)
  - The dual-axis chart allows for simultaneous visualization of total fatalities and fatalities per 100,000 population, providing a clearer understanding of trends.
 
- **Save Chart:** Exports the dual-axis chart as an image file (fatality_analysis_chart.png) to the data folder.

### Code Used to conduct analysis:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data from CSV files
fatalities_df = pd.read_csv(
    r"c:\Users\eCron\OneDrive\Documents\ATU_CourseWork\Web Services and Applications\Assessments\Project\WSAA-Project\data\five_yr_fatalities.csv"
)
population_df = pd.read_csv(
    r"c:\Users\eCron\OneDrive\Documents\ATU_CourseWork\Web Services and Applications\Assessments\Project\WSAA-Project\data\population_breakdown.csv"
)

# Calculate yearly fatality totals
yearly_fatalities = fatalities_df.groupby("Year")["Fatalities"].sum().reset_index()

# Merge with population data
merged_df = pd.merge(yearly_fatalities, population_df, left_on="Year", right_on="Year")

# Calculate fatalities per capita and per 100,000 population
merged_df["Fatalities per Capita"] = merged_df["Fatalities"] / (merged_df["Population (Thousand)"] * 1000)
merged_df["Fatalities per 100,000"] = (merged_df["Fatalities"] / (merged_df["Population (Thousand)"] * 1000)) * 100000

# Output results
print(merged_df[["Year", "Fatalities", "Fatalities per Capita", "Fatalities per 100,000"]])

# Save results to a new CSV file
output_path = r"c:\Users\eCron\OneDrive\Documents\ATU_CourseWork\Web Services and Applications\Assessments\Project\WSAA-Project\data\fatality_analysis.csv"
merged_df.to_csv(output_path, index=False)

# Plot total fatalities as a bar chart
plt.figure(figsize=(10, 6))
plt.bar(merged_df["Year"], merged_df["Fatalities"], color="skyblue", label="Total Fatalities")
plt.xlabel("Year")
plt.ylabel("Total Fatalities")
plt.title("Yearly Fatalities")
plt.legend()
plt.show()

# Plot fatalities per 100,000 as a line chart
plt.figure(figsize=(10, 6))
plt.plot(merged_df["Year"], merged_df["Fatalities per 100,000"], marker="o", color="orange", label="Fatalities per 100,000")
plt.xlabel("Year")
plt.ylabel("Fatalities per 100,000")
plt.title("Fatalities per 100,000 Population")
plt.legend()
plt.show()

# Dual-axis chart: Total Fatalities (bar) and Fatalities per 100,000 (line)
fig, ax1 = plt.subplots(figsize=(10, 6))

# Bar chart for total fatalities
ax1.bar(merged_df["Year"], merged_df["Fatalities"], color="skyblue", label="Total Fatalities")
ax1.set_xlabel("Year")
ax1.set_ylabel("Total Fatalities", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

# Line chart for fatalities per 100,000
ax2 = ax1.twinx()
ax2.plot(merged_df["Year"], merged_df["Fatalities per 100,000"], marker="o", color="orange", label="Fatalities per 100,000")
ax2.set_ylabel("Fatalities per 100,000", color="orange")
ax2.tick_params(axis="y", labelcolor="orange")

fig.suptitle("Yearly Fatalities and Fatalities per 100,000 Population")
fig.tight_layout()

# Save the chart to the data folder
output_chart_path = r"c:\Users\eCron\OneDrive\Documents\ATU_CourseWork\Web Services and Applications\Assessments\Project\WSAA-Project\data\fatality_analysis_chart.png"
plt.savefig(output_chart_path)

plt.show()
```

### Insights on Fatalities and Population Data

![terminal_output_fatalities_per_capita.png](./data/terminal_output_fatalities_per_capita.png)

1. **Yearly Fatalities**: The total number of fatalities as displayed in the 'terminal_output_fatalities_per_capita.png' image varies each year, with the highest being 180 in 2023 and the lowest being 132 in 2021.

2. **Population Growth**: The population increases steadily each year, starting at 5,029.9 thousand in 2020 and reaching 5,380.3 thousand in 2024.

3. **Fatalities per Capita**: This metric, which represents fatalities relative to the total population, is very small (in the range of 0.00003) and increases slightly over the years.

4. **Fatalities per 100,000 Population**: This metric provides a normalized view of fatalities, making it easier to compare across years. It ranges from 2.60 in 2021 to 3.41 in 2023.

5. **Trend in Fatalities**: Fatalities generally increase from 2021 to 2023, peaking in 2023, before slightly decreasing in 2024.

6. **Population Impact**: Despite the growing population, the fatalities per capita and per 100,000 population show that the rate of fatalities is not directly proportional to population growth.

7. **Lowest Fatality Rate**: The year 2021 has the lowest fatalities per 100,000 population (2.60), indicating a relatively safer year compared to others.

8. **Highest Fatality Rate**: The year 2023 has the highest fatalities per 100,000 population (3.41), suggesting a significant increase in fatalities relative to the population.

9. **Fatalities vs. Population**: While the population grows steadily, the number of fatalities does not follow a consistent trend, indicating other factors influencing fatalities.

10. **Data Normalization**: The inclusion of "Fatalities per Capita" and "Fatalities per 100,000" provides a normalized perspective, making it easier to compare the impact of fatalities across years with varying population sizes.

## PART C : CRUD API

A functional CRUD API for managing road fatalities data using Flask and Flask-RESTful is designed to efficiently handle Create, Read, Update, and Delete operations on road fatalities records. This API ensures seamless data management and enables users to interact with road fatalities data through a user-friendly and scalable interface. It supports data validation, modular design, and integration with external tools like Postman for testing and documentation, making it suitable for analysis, visualization, and tracking trends over time.

Below are the steps and functionalities implemented in the code:

### 1. Setup and Initialization
**Flask and Flask-RESTful:**
- The Flask framework is used to create the web application.
- Flask-RESTful simplifies the creation of RESTful APIs by providing a Resource class for defining endpoints.
**App Initialization:**
- app = Flask(__name__) initializes the Flask application.
- api = Api(app) initializes the RESTful API.

### 2. In-Memory Data Store
**Purpose:**
- The data_store list is used as a temporary in-memory database to store road fatalities data.
**Each record contains:**
- id: A unique identifier for the record.
- year: The year of the record.
- month: The month of the record.
- fatalities: The number of fatalities for that month.
**Auto-Increment ID:**
The next_id variable ensures that each new record gets a unique id.

### 3. CRUD Operations
The FatalitiesResource class defines the CRUD operations for managing the data.

#### a. READ (GET)
**Functionality:**
- Fetches all records or a specific record by id.
- If an id is provided as a query parameter, it searches for the record with that id.
- If no id is provided, it returns all records.
**Error Handling:**
- Returns a 404 status code with a "Record not found" message if the record does not exist.

#### b. CREATE (POST)
**Functionality:**
- Accepts a JSON payload to create a new record.
- Adds the record to the data_store with a unique id.
**Validation:**
- Ensures that the required fields (year, month, fatalities) are present in the request.
- Validates that fatalities is a non-negative integer.
**Response:**
- Returns a 201 status code with a success message and the created record.

#### c. UPDATE (PUT)
**Functionality:**
- Updates an existing record by id with the provided JSON payload.
- earches for the record with the specified id and updates its fields.
**Error Handling:**
- Returns a 404 status code with a "Record not found" message if the record does not exist.
**Response:**
- Returns a 200 status code with a success message and the updated record.

#### d. DELETE (DELETE)
**Functionality:**
- Deletes a record by id.
- Removes the record from the data_store.
**Error Handling:**
- Returns a 404 status code with a "Record not found" message if the record does not exist.
**Response:**
- Returns a 200 status code with a success message.

### 4. API Routes

**Endpoints:**
- /api/fatalities: Handles GET and POST requests.
- /api/fatalities/<int:record_id>: Handles PUT and DELETE requests for a specific record by id.

**Route Registration:**
api.add_resource(FatalitiesResource, '/api/fatalities', '/api/fatalities/<int:record_id>') registers the resource with the specified routes.

### 5. Running the Application
**Debug Mode:**
- The application runs in debug mode (app.run(debug=True)), which provides detailed error messages and auto-reloads the server during development.
**Access:**
- The API is accessible at http://127.0.0.1:5000/api/fatalities.

### Code used
The following is the code used

```python
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_cors import CORS  # Import CORS
import pandas as pd  # Import pandas for reading CSV files

app = Flask(__name__)
CORS(app)  # Enable CORS for the entire app
api = Api(app)

# Path to the CSV file
csv_file_path = "../data/five_yr_fatalities.csv"

# Load data from the CSV file
try:
    df = pd.read_csv(csv_file_path)
    data_store = df.to_dict(orient="records")  # Convert DataFrame to a list of dictionaries
except FileNotFoundError:
    data_store = []  # If the file is not found, initialize an empty data store

# Auto-increment ID for new entries
next_id = len(data_store) + 1

# API Resource for CRUD operations
class FatalitiesResource(Resource):
    # READ: Get all records or a specific record by ID
    def get(self):
        record_id = request.args.get('id')
        if record_id:
            record = next((item for item in data_store if item["id"] == int(record_id)), None)
            if record:
                return record, 200
            return {"message": "Record not found"}, 404
        return data_store, 200

    # CREATE: Add a new record
    def post(self):
        global next_id
        new_record = request.json

        # Validation
        if not all(k in new_record for k in ("year", "month", "fatalities")):
            return {"message": "Missing required fields"}, 400
        if not isinstance(new_record["fatalities"], int) or new_record["fatalities"] < 0:
            return {"message": "Invalid fatalities value"}, 400

        new_record["id"] = next_id
        data_store.append(new_record)
        next_id += 1
        return {"message": "Record created successfully", "record": new_record}, 201

    # UPDATE: Update an existing record by ID
    def put(self, record_id):
        record = next((item for item in data_store if item["id"] == record_id), None)
        if not record:
            return {"message": "Record not found"}, 404

        updated_data = request.json
        record.update(updated_data)
        return {"message": "Record updated successfully", "record": record}, 200

    # DELETE: Delete a record by ID
    def delete(self, record_id):
        global data_store
        record = next((item for item in data_store if item["id"] == record_id), None)
        if not record:
            return {"message": "Record not found"}, 404

        data_store = [item for item in data_store if item["id"] != record_id]
        return {"message": "Record deleted successfully"}, 200


# Add routes to the API
api.add_resource(FatalitiesResource, '/api/fatalities', '/api/fatalities/<int:record_id>')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
```

### Terminal Output

When the application was running, the terminal displayed the following messages.  
```
* Restarting with watchdog (windowsapi)
* Debugger is active!
* Debugger PIN: 397-799-927 
```

The following image captures output when API Usage is performed.

![Image of Terminal Output](./data/terminal_message_crud_api.png)

#### API Usage

##### 1. Create a New Record
**Request:**
```
POST http://127.0.0.1:5000/api/fatalities
Content-Type: application/json

{
    "year": 2021,
    "month": "April",
    "fatalities": 18
}
```
**Response:**
```
{
    "message": "Record created successfully",
    "record": {
        "year": 2021,
        "month": "April",
        "fatalities": 18,
        "id": 4
    }
}
```

##### 2. Read All records
**Request:**
```
GET /api/fatalities
```
**Response**
```
[
    { "id": 1, "year": 2020, "month": "January", "fatalities": 9 },
    { "id": 2, "year": 2020, "month": "February", "fatalities": 19},
    { "id": 3, "year": 2020, "month": "March", "fatalities": 17 },
    { "year": 2021, "month": "April", "fatalities": 18, "id": 4 }
]
```

##### 3. Update a Record
**Request:**
```
PUT /api/fatalities/2
Content-Type: application/json

{
    "fatalities": 20
}
```
**Response**
```
{
    "message": "Record updated successfully",
    "record": {
        "id": 2,
        "year": 2020,
        "month": "February",
        "fatalities": 20
    }
}
```

##### 3. Delete a Record
**Request:**
```
DELETE /api/fatalities/3
```
**Response**
```
{
    "message": "Record deleted successfully"
}
```

### References
**Flask Documentation**
[Flask Official Documentation](https://flask.palletsprojects.com/en/stable/)
Provides detailed information on how to build web applications using Flask.

**Flask-RESTful Documentation**
[Flask-RESTful Documentation](https://flask-restful.readthedocs.io/en/latest/)
Explains how to create RESTful APIs using Flask-RESTful, including the Resource class and route management.

**Postman Documentation**
[Postman Documentation](https://www.postman.com/)
Useful for testing CRUD API endpoints.

**Python Requests Library**
[Requests Library Documentation](https://requests.readthedocs.io/en/latest/)
Covers how to make HTTP requests and handle responses, which is useful for testing APIs programmatically.

## Part D : Frontend Development

The frontend of the project was designed to provide a user-friendly web interface for visualizing road safety data. It allows users to view monthly road fatalities over the last five years in both tabular and graphical formats. The interface dynamically fetches data from the backend API and updates the table and chart without requiring a page reload.

### Purpose
**Create a User-Friendly Web Interface:**
- Provide an intuitive and visually appealing interface for users to interact with the data.
- Display road fatalities data in a clear and organized table.
- Visualize trends in road fatalities using a line chart.
**Use jQuery and AJAX for Asynchronous Data Retrieval:**
- Fetch data dynamically from the backend API (/api/grouped-fatalities) without reloading the page.
- Ensure seamless integration between the frontend and backend.

### Implementation
**HTML Structure:**
The index.html file provides the structure for the web interface, including:
-  A table (#fatalitiesTable) to display monthly fatalities data.
-  A chart (#fatalitiesChart) to visualize trends in fatalities.
**Dynamic Data Handling:**
- The app.js file uses jQuery and AJAX to fetch data from the backend API and dynamically populate the table and chart.
**Chart Visualization:**
- The Chart.js library is used to render a line chart that shows monthly fatalities over the last five years.
**Styling:**
- The styles.css file ensures the interface is visually appealing and easy to navigate

### Steps to Run the Frontend
1. Ensure the backend API (05_app.py) is running (Flask app).
- Open a terminal, navigate to the directory containing the backend file, and execute:
```python
python 05_app.py
```
- Confirm the API is accessible at
```
http://127.0.0.1:5000/api/grouped-fatalities
```

2. Verify Frontend Files
- Ensure the following files are in the static folder:
  - index.html in the static directory.
  - styles.css in the static/css directory.
  - app.js in the static/js directory.

3. Open the Frontend in a Browser
 - Open the index.html file in a web browser (e.g., Chrome, Firefox).
 - Use a local web server if necessary (e.g., Python's HTTP server):
 ```python
python -m http.server
```
Navigate to http://127.0.0.1:8000/static/index.html in the browser.

4. Verify Data Fetching 
 - Check the browser console (Developer Tools > Console) for any errors.
 - Ensure the table and chart are populated with data fetched from the backend API.

5. Inspect the Table
- Verify that the table (#fatalitiesTable) displays the correct data:
 - Columns: ID, Year, Month, Fatalities.
 - Rows dynamically populated with API data.

 6. Inspect the Chart
 - Confirm that the chart renders correctly:
 - A line chart showing monthly fatalities over the last five years.
 - Labels and data points match the API data.

7. Interact with the Interface
- Users can interact with the chart and table to view trends in road fatalities.
- Data is fetched asynchronously, allowing for real-time updates without page reloads.

### Outcome
**1. User-Friendly Web Interface:**
- The interface successfully displays road fatalities data in a table and a line chart.
- Users can easily view trends and patterns in the data.
**2. Seamless Asynchronous Data Retrieval:**
- Data is fetched dynamically from the backend API using jQuery and AJAX.
- The table and chart update automatically without requiring a page reload.
**3.Visualization of Trends:**
- The line chart provides a clear visualization of monthly fatalities trends over the last five years.
- The table complements the chart by providing detailed numerical data.

### Screenshots
Image 'monthly_fatalities_over_the_last_5_years.png' displays an interactive chart with data displayed by hovering over each monthly point accessible at http://127.0.0.1:5500/WSAA-Project/static/index.html
![Monthly Fatalities Image](./data/monthly_fatalites_over_the_last_5_years.png)

Image 'Fatalities_Data.png' displays a chart with headings 'ID, Year, Month, Fatalities' which is accessed at http://127.0.0.1:5500/WSAA-Project/static/index.html
![Fatalities Data](./data/fatalities_data.png)

This interface is intuitive, visually appealing, and effectively displays the data in both tabular and graphical formats.  Data is dynamically fetched from the backend API and displayed in real-time without requiring a page reload.  This method of accessing data is preferred as it negates the necessity to re run programs when CRUD actions are undertaken.

## Part E: OAuth (Open Authorization)

OAuth (Open Authorization) is an open standard protocol that allows secure, delegated access to resources on behalf of a user. It is commonly used to grant third-party applications limited access to a user's resources (e.g., data or services) without exposing the user's credentials (like passwords).

OAuth was not considered necessary in this project for the following reasons

**Private Repository:**
- A private GitHub repository is already secure and accessible only to authorized users with the appropriate permissions.
- GitHub handles authentication and access control for private repositories, so additional layers like OAuth are redundant in this context.

**No Public API Exposure:**
- If the API is not being hosted on a public server and is only being used locally (e.g., http://127.0.0.1:5000), there is no need for OAuth since the API is not exposed to external users.

**Limited Scope:**
- The project is focused on analyzing and visualizing road safety data, with CRUD operations on a local dataset. There is no sensitive or user-specific data that requires advanced authentication mechanisms like OAuth.

**Development and Testing Context:**
The project is primarily for coursework, development, or testing purposes, implementing OAuth would add unnecessary complexity without providing significant benefits.

## References

- [OAuth 2.0 Authorization Framework (RFC 6749)](https://datatracker.ietf.org/doc/html/rfc6749)  
  The official specification for OAuth 2.0, detailing the protocol and its components.
- [OAuth 2.0 Simplified](https://aaronparecki.com/oauth-2-simplified/)  
  A beginner-friendly guide to understanding OAuth 2.0.
- [OAuth.net](https://oauth.net/)  
  A comprehensive resource for learning about OAuth, including tutorials and libraries.
- [Google Identity Platform OAuth 2.0 Documentation](https://developers.google.com/identity/protocols/oauth2)  
  Google's implementation of OAuth 2.0 for accessing Google APIs.
- [Microsoft Identity Platform OAuth 2.0 Documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow)  
  Microsoft's guide to implementing OAuth 2.0 for Azure and Microsoft services.

#### Acknowledgements
Github Copilot. "This work was partially supported by GitHub Copilot, an AI-powered code completion tool developed by GitHub, which assisted in generating parts of the code."

## Project References

- [Chart.js Documentation](https://www.chartjs.org/docs/latest/)
- [CURL Documentation](https://curl.se/)
- [Flask Official Documentation](https://flask.palletsprojects.com/en/stable/)
- [Flask-RESTful Documentation](https://flask-restful.readthedocs.io/en/latest/)
- [GitHub Copilot](https://github.com/features/copilot)
- [Google Identity Platform OAuth 2.0 Documentation](https://developers.google.com/identity/protocols/oauth2)
- [JSON-stat Format](https://json-stat.org/)
- [Markdown Guide](https://www.markdownguide.org/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Microsoft Identity Platform OAuth 2.0 Documentation](https://learn.microsoft.com/en-us/azure/active-directory/develop/v2-oauth2-auth-code-flow)
- [OAuth 2.0 Authorization Framework (RFC 6749)](https://datatracker.ietf.org/doc/html/rfc6749)
- [OAuth 2.0 Simplified](https://aaronparecki.com/oauth-2-simplified/)
- [OAuth.net](https://oauth.net/)
- [OS Module in Python](https://docs.python.org/3/library/os.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Postman Documentation](https://www.postman.com/)
- [Python CSV Module Documentation](https://docs.python.org/3/library/csv.html)
- [Requests Library Documentation](https://requests.readthedocs.io/en/latest/)
- [Seaborn Documentation](https://seaborn.pydata.org/)

# END