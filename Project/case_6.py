import pandas as pd
import os

# Create reports folder if not exists
os.makedirs('reports', exist_ok=True)

# Load data
orders = pd.read_csv("processed_orders.csv")
products = pd.read_csv("products.csv")
customers = pd.read_csv("customers.csv")

# Merge orders with products and customers to get full info
df = orders.merge(products, on="ProductID", how="left")
df = df.merge(customers, on="CustomerID", how="left")

# Convert OrderDate to datetime
df['OrderDate'] = pd.to_datetime(df['OrderDate'])

# Add OrderMonth column (YYYY-MM)
df['OrderMonth'] = df['OrderDate'].dt.to_period('M').astype(str)

# 1. Total revenue by product category
revenue_by_category = df.groupby('Category')['TotalPrice'].sum().reset_index()
revenue_by_category = revenue_by_category.sort_values(by='TotalPrice', ascending=False)
revenue_by_category.to_csv("reports/revenue_by_category.csv", index=False)

# 2. Top 3 customers by spending
spending_by_customer = df.groupby(['CustomerID', 'Name'])['TotalPrice'].sum().reset_index()
top_customers = spending_by_customer.sort_values(by='TotalPrice', ascending=False).head(3)
top_customers.to_csv("reports/top_three_customers.csv", index=False)

# 3. Monthly revenue trends
monthly_revenue = df.groupby('OrderMonth')['TotalPrice'].sum().reset_index()
monthly_revenue.to_csv("reports/monthly_revenue_trends.csv", index=False)

print("Reports are generated and saved to the reports/ folder.")