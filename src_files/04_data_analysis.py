# 04_data_analysis.py
# This script analyzes road fatalities data over the last five years.
# It loads the data from a CSV file, groups it by year and month, detects trends, and visualizes the results.
# Author: Edward Cronin (g00425645)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Define the path to the input CSV file containing road fatality data
csv_file = os.path.join(os.path.dirname(__file__), "../data/five_yr_fatalities.csv")

try:
    # Load data from CSV file into a DataFrame
    fatality_data = pd.read_csv(csv_file)
    print("Data successfully loaded!")
except FileNotFoundError:
    print(f"Error: File {csv_file} not found.")
    exit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit()

# Group and aggregate data by Year and Month to calculate total fatalities
grouped_fatality_data = fatality_data.groupby(["Year", "Month"], as_index=False).sum()

# Sort the data by Year and Month for proper visualization
month_order = [
    "January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"
]
grouped_fatality_data["Month"] = pd.Categorical(
    grouped_fatality_data["Month"], categories=month_order, ordered=True
)
grouped_fatality_data = grouped_fatality_data.sort_values(by=["Year", "Month"])

# Detect trends (increases or decreases) in fatalities
grouped_fatality_data["Change"] = grouped_fatality_data["Fatalities"].diff().fillna(0)
grouped_fatality_data["Trend"] = grouped_fatality_data["Change"].apply(
    lambda x: "Increase" if x > 0 else "Decrease" if x < 0 else "No Change"
)

# Save the trend data to a CSV file
trend_data_file = os.path.join(os.path.dirname(__file__), "../data/fatality_trends.csv")
try:
    grouped_fatality_data.to_csv(trend_data_file, index=False)
    print(f"Trend data successfully saved to {trend_data_file}")
except Exception as e:
    print(f"Error while saving trend data: {e}")
    exit()

# Create line plot for fatalities grouped by Year and Month
plt.figure(figsize=(12, 6))
sns.lineplot(data=grouped_fatality_data, x="Month", y="Fatalities", hue="Year", marker="o")

# Add vertical lines to split quarters
quarter_splits = ["March", "June", "September"]
for quarter in quarter_splits:
    plt.axvline(x=quarter, color="red", linestyle="--", alpha=0.7)

# Annotate quarters on the graph
quarters = {"Q1": 1.5, "Q2": 4.5, "Q3": 7.5, "Q4": 10.5}
for quarter, position in quarters.items():
    plt.text(position, grouped_fatality_data["Fatalities"].max() + 2, quarter, ha="center", fontsize=10, color="black")

# Annotate each data point with fatality count
for _, row in grouped_fatality_data.iterrows():
    plt.text(row["Month"], row["Fatalities"] + 0.5, str(row["Fatalities"]), ha="center", fontsize=8)

# Chart details and formatting
plt.title("Monthly Road Fatalities Over the Last 5 Years with Quarterly Splits")
plt.xlabel("Month")
plt.ylabel("Fatalities")
plt.legend(title="Year")
plt.xticks(rotation=45)
plt.tight_layout()

# Save the graph to the output directory
graph_file = os.path.join(os.path.dirname(__file__), "../data/fatalities_trend_graph.png")
try:
    plt.savefig(graph_file)
    print(f"Graph successfully saved to {graph_file}")
except Exception as e:
    print(f"Error while saving graph: {e}")
    exit()

plt.show()
