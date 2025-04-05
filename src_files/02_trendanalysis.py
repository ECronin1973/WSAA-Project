import pandas as pd
import os

# Define the relative path to the input CSV file containing road fatalities data
csv_file = os.path.join(os.path.dirname(__file__), "../data/road_fatalities.csv")

try:
    # Load data from the CSV file into a DataFrame
    data_frame = pd.read_csv(csv_file)
except FileNotFoundError:
    print(f"Error: The file {csv_file} does not exist.")
    exit()
except Exception as e:
    print(f"An unexpected error occurred while reading the file: {e}")
    exit()

# Split the "Month" column into separate "Year" and "Month" columns
# This assumes the "Month" column is in the format "Year Month" (e.g., "2024 January")
data_frame[["Year", "Month"]] = data_frame["Month"].str.extract(r"(\d{4})\s+(.*)")

# Filter the DataFrame to include rows for the last five years dynamically
current_year = 2024  # Replace this with dynamic calculation if needed
filtered_data = data_frame[data_frame["Year"].astype(int).between(current_year - 4, current_year)]

# Define the output directory and file path for saving the filtered data
output_dir = os.path.join(os.path.dirname(__file__), "../data")
output_file = os.path.join(output_dir, "five_yr_fatalities.csv")
os.makedirs(output_dir, exist_ok=True)  # Create the directory if it doesn't exist

try:
    # Save the filtered data to a new CSV file
    filtered_data.to_csv(output_file, index=False)
    print(f"Filtered data successfully saved to {output_file}")
except Exception as e:
    print(f"An error occurred while writing the file: {e}")
    exit()
