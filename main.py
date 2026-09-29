from fastapi import FastAPI
from database import db

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Restaurant API is running"}