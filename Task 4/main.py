import pandas as pd
import matplotlib.pyplot as plt

# Load file (after upload in Colab)
df = pd.read_csv("sales_data.csv")

# Clean column names
df.columns = df.columns.str.strip().str.lower()

print("Columns:", df.columns)

# -----------------------------
# 🧹 DATA CLEANING
# -----------------------------
df.dropna(inplace=True)

# -----------------------------
# 📊 BAR CHART (Sales by Product)
# -----------------------------
product_sales = df.groupby('product')['total_sales'].sum()

plt.figure()
product_sales.plot(kind='bar')
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# -----------------------------
# 📈 LINE CHART (Monthly Trend)
# -----------------------------
df['date'] = pd.to_datetime(df['date'])
df['month'] = df['date'].dt.month

monthly_sales = df.groupby('month')['total_sales'].sum()

plt.figure()
monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.grid()
plt.show()

# -----------------------------
# 🥧 PIE CHART (Region Distribution)
# -----------------------------
region_sales = df.groupby('region')['total_sales'].sum()

plt.figure()
region_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales Distribution by Region")
plt.ylabel("")
plt.show()

# -----------------------------
# 📊 ANALYSIS OUTPUT
# -----------------------------
print("\n📊 RESULTS")
print("Total Sales:", df['total_sales'].sum())
print("Average Sales:", df['total_sales'].mean())
print("Top Product:", product_sales.idxmax())
print("Best Region:", region_sales.idxmax())