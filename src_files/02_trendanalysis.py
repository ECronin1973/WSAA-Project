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
# The filtered data is now saved in the CSV file, ready for further analysis or visualization.