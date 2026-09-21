from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    course: str

@app.post("/students")
def create_student(student: Student):
    return {
        "message": "student created",
        "student": student
    }


class Product(BaseModel):
    name: str
    price: int
    quantity: int

@app.post("/products")
def create_product(product: Product):
    return{
        "message": "product created successfully",
        "product":product
    }
