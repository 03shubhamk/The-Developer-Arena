# Sales Data Analysis Report

## Project Overview

This project analyzes a sales dataset using the Pandas library in Python.

The objective is to understand sales performance by calculating important business metrics and generating a clean report.

---

## Technologies Used

- Python 3
- Pandas

---

## Dataset Information

- Rows: 100
- Columns: 7

Columns:

- Date
- Product
- Quantity
- Price
- Customer_ID
- Region
- Total_Sales

---

## Analysis Steps

### 1. Load Dataset

The CSV file is loaded using pandas.

```python
df = pd.read_csv("sales_data.csv")
```

### 2. Explore Dataset

The following information is checked:

- Shape
- Column Names
- Data Types
- First Five Rows

---

### 3. Data Cleaning

- Checked for missing values.
- Filled missing numerical values using mean.
- Filled missing text values with "Unknown".
- Removed duplicate records.

---

### 4. Sales Analysis

The following metrics were calculated:

- Total Revenue
- Average Sales
- Highest Sale
- Lowest Sale
- Best Selling Product
- Sales by Region

---

## Findings

The program identifies:

- Overall business revenue.
- Most sold product.
- Region generating maximum revenue.
- Average transaction value.
- Highest and lowest sales.

---

## Project Structure

```
Sales_Data_Analysis/
│
├── sales_analysis.py
├── sales_data.csv
├── analysis_report.md
├── requirements.txt
└── screenshots/
```

---

## How to Run

Install dependencies

```
pip install -r requirements.txt
```

Run

```
python sales_analysis.py
```

---

## Output

The program prints a formatted report including:

- Dataset Information
- Missing Values
- Total Revenue
- Best Selling Product
- Region-wise Sales
- Statistical Summary

---

## Conclusion

This project demonstrates basic data analysis using Pandas and introduces important concepts like data exploration, cleaning, aggregation, and business reporting.
