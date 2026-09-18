from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my API"}


@app.get("/user")
def user():
    return {
        "name": "Raghu",
        "age": 24,
        "course": "Python",
        "city": "Rajahmundry"
    }