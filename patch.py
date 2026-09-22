#post put and get

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Product(BaseModel):
    name: str
    price: float
    quantity: int


products= [
    {
        "name": "laptop",
        "price": 49999,
        "quantity": 4
    },
    {
        "name": "mobile",
        "price": 29999,
        "quantity": 3
    },
    {
        "name": "keyboard",
        "price": 19999,
         "quantity": 5
    }
]

@app.get("/product")
def create_products():
    return products

@app.post("/product")
def create_product():

    new_product = {
        "name": "Headphones",
        "price": 2999,
        "quantity": 12

    }

    products.append(new_product)

    return {
        "message": "product created successfully",
        "product": new_product
    }

@app.put("/product")
def update_product(updated_product: Product):

    products[0]["name"] = updated_product.name
    products[0]["price"] = updated_product.price
    products[0]["quantity"] = updated_product.quantity

    return {
        "message": "Product updated successfully",
        "product": products[0]
    }

@app.delete("/products")

def delete_product(product_name: str):

    for index, product in enumerate(products):

        if product["name"] == product_name:
            deleted_product = products.pop(index)

            return {
                "message": "product deleted successfully",
                "product": deleted_product
            }

    return {
        "message": "product not found"
    }

class ProductUpdate(BaseModel):
    name: str | None = None
    price: float | None = None
    quantity: int | None = None
    
@app.patch("/product")
def patch_product(product_name: str, update: ProductUpdate):

    for product in products:

        if product["name"] == product_name:

            if update.name is not None:
                product["name"] = update.name

            if update.price is not None:
                product["price"] = update.price

            if update.quantity is not None:
                product["quantity"] = update.quantity

            return {
                "message": "Product partially updated",
                "product": product
            }

    return {
        "message": "Product not found"
    }