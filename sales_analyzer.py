import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("sales.csv")

# Preview the dataset
print("📊 Original Data:")
print(df.head())

# Step 1: Handle missing values
df['Sales'].fillna(df['Sales'].mean(), inplace=True)
df['Region'].fillna("Unknown", inplace=True)

# Step 2: Add new column for Revenue
df['Revenue'] = df['Sales'] * df['Price']

# Step 3: Group by Product and summarize
product_summary = df.groupby('Product').agg({
    'Sales': 'sum',
    'Revenue': 'sum'
}).sort_values(by='Revenue', ascending=False)

print("\n💰 Product Summary:")
print(product_summary)

# Step 4: Top 5 selling products
top_5 = product_summary.head(5)
top_5.plot(kind='bar', y='Revenue', title="Top 5 Products by Revenue", legend=False)
plt.ylabel('Revenue')
plt.tight_layout()
plt.show()

# Step 5: Average sales per region
avg_sales = df.groupby('Region')['Sales'].mean()
print("\n📌 Average Sales by Region:")
print(avg_sales)
