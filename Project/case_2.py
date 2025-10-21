from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Product(BaseModel):
    ProductID: str
    ProductName: str
    Category: str
    Price: float

products_db = [
    {"ProductID":"P101","ProductName":"Laptop","Category":"Electronics","Price":800},
    {"ProductID":"P102","ProductName":"Mouse","Category":"Accessories","Price":20},
    {"ProductID":"P103","ProductName":"Keyboard","Category":"Accessories","Price":35},
    {"ProductID":"P104","ProductName":"Headphones","Category":"Audio","Price":50}
]
@app.get("/products", response_model=List[Product])
def get_products():
    return products_db

@app.post("/products")
def add_product(product: Product):
    products_db.append(product)
    return {"message": "Product added"}

@app.put("/products/{id}")
def update_product(id: str, updated: Product):
    for i, p in enumerate(products_db):
        if p.ProductID == id:
            products_db[i] = updated
            return {"message": "Product updated"}
    return {"error": "Product not found"}

@app.delete("/products/{id}")
def delete_product(id: str):
    global products_db
    products_db = [p for p in products_db if p.ProductID != id]
    return {"message": "Product deleted"}