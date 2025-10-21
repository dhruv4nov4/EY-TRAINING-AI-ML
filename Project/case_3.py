import pandas as pd
customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")
orders = pd.read_csv("orders.csv")

# Merge all data
merged = orders.merge(customers, on="CustomerID").merge(products, on="ProductID")

# Add TotalPrice and OrderMonth
merged["TotalPrice"] = merged["Quantity"] * merged["Price"]
merged["OrderMonth"] = pd.to_datetime(merged["OrderDate"]).dt.month

# Save processed file
merged.to_csv("processed_orders.csv", index=False)