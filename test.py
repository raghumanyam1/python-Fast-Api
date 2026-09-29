from fastapi import FastAPI
import time

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Test server"}

@app.get("/slow")
def slow_api():
    time.sleep(0.2)
    return{"message": "slow api response"}