# 06_analyze_fatalities.py
# This script analyzes road fatalities data over the last five years.
# It loads the data from CSV files, calculates fatalities per capita, and visualizes the results.
# Author: Edward Cronin (g00425645)

import pandas as pd
import matplotlib.pyplot as plt
import os

# Define file paths for input data
fatalities_file = r"c:\Users\eCron\OneDrive\Documents\ATU_CourseWork\Web Services and Applications\Assessments\Project\WSAA-Project\data\five_yr_fatalities.csv"
population_file = r"c:\Users\eCron\OneDrive\Documents\ATU_CourseWork\Web Services and Applications\Assessments\Project\WSAA-Project\data\population_breakdown.csv"

try:
    # Load fatality data and population data from CSV files
    fatalities_df = pd.read_csv(fatalities_file)
    population_df = pd.read_csv(population_file)
    print("Data successfully loaded!")
except FileNotFoundError as e:
    print(f"Error: File not found. {e}")
    exit()
except pd.errors.EmptyDataError as e:
    print(f"Error: File is empty or invalid. {e}")
    exit()
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    exit()

# Calculate yearly fatality totals
yearly_fatalities = fatalities_df.groupby("Year")["Fatalities"].sum().reset_index()

try:
    # Merge yearly fatalities with population data
    merged_df = pd.merge(yearly_fatalities, population_df, on="Year")
except KeyError as e:
    print(f"Error: Failed to merge dataframes. {e}")
    exit()

# Calculate fatalities per capita and per 100,000 population
merged_df["Fatalities per Capita"] = merged_df["Fatalities"] / (merged_df["Population (Thousand)"] * 1000)
merged_df["Fatalities per 100,000"] = (merged_df["Fatalities"] / (merged_df["Population (Thousand)"] * 1000)) * 100000

# Save results to a new CSV file
output_csv_path = r"c:\Users\eCron\OneDrive\Documents\ATU_CourseWork\Web Services and Applications\Assessments\Project\WSAA-Project\data\fatality_analysis.csv"
try:
    merged_df.to_csv(output_csv_path, index=False)
    print(f"Analysis results saved to {output_csv_path}")
except Exception as e:
    print(f"Error while saving analysis results: {e}")
    exit()

# Function for bar chart visualization
def plot_bar_chart(data, x, y, title, xlabel, ylabel, save_path, color="skyblue"):
    plt.figure(figsize=(10, 6))
    plt.bar(data[x], data[y], color=color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    try:
        plt.savefig(save_path)
        print(f"Chart saved to {save_path}")
    except Exception as e:
        print(f"Error while saving chart: {e}")
    plt.show()

# Plot total fatalities bar chart
plot_bar_chart(
    merged_df,
    x="Year",
    y="Fatalities",
    title="Yearly Fatalities",
    xlabel="Year",
    ylabel="Total Fatalities",
    save_path=r"c:\Users\eCron\OneDrive\Documents\ATU_CourseWork\Web Services and Applications\Assessments\Project\WSAA-Project\data\yearly_fatalities_chart.png"
)

# Plot fatalities per 100,000 line chart
plt.figure(figsize=(10, 6))
plt.plot(merged_df["Year"], merged_df["Fatalities per 100,000"], marker="o", color="orange")
plt.xlabel("Year")
plt.ylabel("Fatalities per 100,000")
plt.title("Fatalities per 100,000 Population")
plt.tight_layout()
try:
    plt.savefig(r"c:\Users\eCron\OneDrive\Documents\ATU_CourseWork\Web Services and Applications\Assessments\Project\WSAA-Project\data\fatalities_per_100k_chart.png")
    print("Fatalities per 100,000 chart saved successfully.")
except Exception as e:
    print(f"Error while saving fatalities per 100,000 chart: {e}")
plt.show()
