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