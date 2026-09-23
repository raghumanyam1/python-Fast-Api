from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    quantity: int

products = [
    {
        "id": 1,
        "name": "laptop",
        "price": 49999,
        "quantity": 4
    },
    {
        "id": 2,
        "name": "mobile",
        "price": 29999,
        "quantity": 6
    }
]

@app.post("/products")
def create_product(product: Product):

    new_product = {
        "id": len(products) + 1,
        "name": product.name,
        "price": product.price,
        "quantity": product.quantity
    }

    products.append(new_product)

    return {
        "message": "Product created successfully",
        "product": new_product
    }


# ---------------- READ ALL ----------------
@app.get("/products")
def get_products():

    return products


# ---------------- READ ONE ----------------
@app.get("/products/{product_id}")
def get_product(product_id: int):

    for product in products:
        if product["id"] == product_id:
            return product

    return {"message": "Product not found"}


# ---------------- UPDATE ----------------
@app.put("/products/{product_id}")
def update_product(product_id: int, product: Product):

    for item in products:

        if item["id"] == product_id:

            item["name"] = product.name
            item["price"] = product.price
            item["quantity"] = product.quantity

            return {
                "message": "Product updated successfully",
                "product": item
            }

    return {"message": "Product not found"}


# ---------------- DELETE ----------------
@app.delete("/products/{product_id}")
def delete_product(product_id: int):

    for product in products:

        if product["id"] == product_id:

            products.remove(product)

            return {
                "message": "Product deleted successfully"
            }

    return {"message": "Product not found"}