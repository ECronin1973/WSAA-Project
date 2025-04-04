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
