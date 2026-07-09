"""
Project: Sales Data Analysis
Internship: The Developers Arena
Author: Shubham Khadekar

Description:
This program loads a sales dataset, explores the data,
cleans it, performs analysis, and generates a report.
"""

import pandas as pd

# ----------------------------
# Load Dataset
# ----------------------------
print("=" * 50)
print("        SALES DATA ANALYSIS")
print("=" * 50)

df = pd.read_csv("sales_data.csv")

# ----------------------------
# Display First Rows
# ----------------------------
print("\nFirst 5 Rows:")
print(df.head())

# ----------------------------
# Dataset Information
# ----------------------------
print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

# ----------------------------
# Missing Values
# ----------------------------
print("\nMissing Values:")
print(df.isnull().sum())

# Fill missing numerical values
numeric_columns = df.select_dtypes(include="number").columns

for col in numeric_columns:
    df[col].fillna(df[col].mean(), inplace=True)

# Fill missing categorical values
categorical_columns = df.select_dtypes(include="object").columns

for col in categorical_columns:
    df[col].fillna("Unknown", inplace=True)

# ----------------------------
# Remove Duplicates
# ----------------------------
duplicates = df.duplicated().sum()
df = df.drop_duplicates()

print(f"\nDuplicates Removed: {duplicates}")

# ----------------------------
# Sales Analysis
# ----------------------------
total_sales = df["Total_Sales"].sum()

average_sales = df["Total_Sales"].mean()

highest_sale = df["Total_Sales"].max()

lowest_sale = df["Total_Sales"].min()

best_selling_product = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
)

top_product = best_selling_product.idxmax()

region_sales = (
    df.groupby("Region")["Total_Sales"]
    .sum()
    .sort_values(ascending=False)
)

# ----------------------------
# Final Report
# ----------------------------
print("\n" + "=" * 50)
print("FINAL SALES REPORT")
print("=" * 50)

print(f"Total Revenue      : ₹{total_sales:,.2f}")
print(f"Average Sale       : ₹{average_sales:,.2f}")
print(f"Highest Sale       : ₹{highest_sale:,.2f}")
print(f"Lowest Sale        : ₹{lowest_sale:,.2f}")

print(f"\nBest Selling Product: {top_product}")

print("\nProducts Sold:")
print(best_selling_product)

print("\nSales by Region:")
print(region_sales)

print("\nAnalysis Completed Successfully.")
