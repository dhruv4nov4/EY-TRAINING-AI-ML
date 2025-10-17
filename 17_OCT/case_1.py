import pandas as pd

# Load CSVs
products = pd.read_csv("products.csv")
customers = pd.read_csv("customers.csv")

# Add a new product
new_product = pd.DataFrame([["P105", "Webcam", "Accessories", 60]], columns=products.columns)
products = pd.concat([products, new_product], ignore_index=True)

# Update product price
products.loc[products["ProductID"] == "P102", "Price"] = 25

# Delete a customer
customers = customers[customers["CustomerID"] != "C002"]

# List all customers from India
indian_customers = customers[customers["Country"] == "India"]
print(indian_customers)