import pandas as pd

# 1. EXTRACT

products = pd.read_csv('products.csv')
customers = pd.read_csv('customers.csv')
orders = pd.read_csv('orders.csv')

# 2. TRANSFORM

# 2.1 JOIN DATASETS
orders_customers = pd.merge(orders, customers, on='CustomerID', how='left')

# Join the result with products on ProductID
full_data = pd.merge(orders_customers, products, on='ProductID', how='left')

# 2.2 ADD NEW COLUMNS


processed_orders.to_csv('processed_orders.csv', index=False)
category_summary.to_csv('category_summary.csv', index=False)
segment_summary.to_csv('segment_summary.csv', index=False)

print("ETL Pipeline completed successfully!")
print("Files generated:")
print(" - processed_orders.csv")
print(" - category_summary.csv")
print(" - segment_summary.csv")