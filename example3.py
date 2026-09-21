from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Fun learn with python"}


@app.get("/students")
def get_students():
    return {
        "students": [
            {"id": 1, "name": "Raghu"},
            {"id": 2, "name": "John"}
        ]
    }