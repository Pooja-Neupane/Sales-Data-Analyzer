import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Step 0: Load CSV file with error handling
try:
    df = pd.read_csv("sales.csv")
    print("✅ CSV file loaded successfully.")
except FileNotFoundError:
    print("❌ Error: 'sales.csv' file not found.")
    exit()

# Preview the dataset
print("\n📊 Original Data (first 5 rows):")
print(df.head())

# Step 1: Handle missing values
df['Sales'] = df['Sales'].fillna(df['Sales'].mean())
df['Region'] = df['Region'].fillna("Unknown")

# Step 2: Add a new 'Revenue' column
if 'Price' in df.columns:
    df['Revenue'] = df['Sales'] * df['Price']
else:
    print("❌ Error: 'Price' column is missing.")
    exit()

# Step 3: Group by Product and summarize
product_summary = (
    df.groupby('Product')
    .agg(Total_Sales=('Sales', 'sum'), Total_Revenue=('Revenue', 'sum'))
    .sort_values(by='Total_Revenue', ascending=False)
)

print("\n💰 Product Summary:")
print(product_summary)

# Step 4: Visualize Top 5 products by Revenue
top_5 = product_summary.head(5)
plt.figure(figsize=(10, 6))
top_5['Total_Revenue'].plot(kind='bar', color='skyblue', edgecolor='black')
plt.title("🏆 Top 5 Products by Revenue", fontsize=14)
plt.ylabel("Revenue", fontsize=12)
plt.xlabel("Product", fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Step 5: Average sales per region
avg_sales = df.groupby('Region')['Sales'].mean().sort_values(ascending=False)
print("\n📌 Average Sales by Region:")
print(avg_sales)

# Optional Step 6: Visualize average sales by region
plt.figure(figsize=(10, 5))
avg_sales.plot(kind='barh', color='lightgreen', edgecolor='black')
plt.title("📍 Average Sales by Region", fontsize=14)
plt.xlabel("Average Sales", fontsize=12)
plt.ylabel("Region", fontsize=12)
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
