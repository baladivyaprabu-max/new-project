import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("data/sample_dataset.csv")

# Display dataset
print("WATER CONSUMPTION DATA")
print(df)

# Explore the dataset
print("\nFirst 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Calculate average consumption using NumPy
average = np.mean(df["Water_Consumption"])
print("\nAverage Water Consumption:", average)

# Bar Chart
plt.figure(figsize=(8, 5))
plt.bar(df["Month"], df["Water_Consumption"])
plt.title("Monthly Water Consumption")
plt.xlabel("Month")
plt.ylabel("Water Consumption")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("bar_chart.png")
plt.show()

# Line Chart
plt.figure(figsize=(8, 5))
plt.plot(df["Month"], df["Water_Consumption"], marker="o")
plt.title("Water Consumption Trend")
plt.xlabel("Month")
plt.ylabel("Water Consumption")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("line_chart.png")
plt.show()

# Pie Chart
plt.figure(figsize=(7, 7))
plt.pie(
    df["Water_Consumption"],
    labels=df["Month"],
    autopct="%1.1f%%"
)
plt.title("Monthly Water Consumption Distribution")
plt.tight_layout()
plt.savefig("pie_chart.png")
plt.show()