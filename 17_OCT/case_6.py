import pandas as pd
import os
df = pd.read_csv("processed_orders_1.csv")
df['TotalPrice']=pd.to_numeric(df['TotalPrice'],errors='coerce')
df['OrderDate']=pd.to_datetime(df['OrderDate'])
os.makedirs("reports", exist_ok=True)
# Total revenue by category
revenue_by_category = merged.groupby("Category")["TotalPrice"].sum()

# Top 3 customers by spending
top_customers = merged.groupby("Name")["TotalPrice"].sum().nlargest(3)

# Monthly revenue trends
monthly_revenue = merged.groupby("OrderMonth")["TotalPrice"].sum()

# Save reports
revenue_by_category.to_csv("reports/revenue_by_category.csv")
top_customers.to_csv("reports/top_customers.csv")
monthly_revenue.to_csv("reports/monthly_revenue.csv")