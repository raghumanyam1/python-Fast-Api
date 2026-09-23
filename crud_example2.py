from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Student model
class Student(BaseModel):
    name: str
    age: int
    course: str


# Temporary database
students = [
    {
        "id": 1,
        "name": "Raghu",
        "age": 24,
        "course": "Python"
    },
    {
        "id": 2,
        "name": "Rahul",
        "age": 23,
        "course": "Java"
    }
]


# CREATE/post
@app.post("/students")
def create_student(student: Student):

    new_student = {
        "id": len(students) + 1,
        "name": student.name,
        "age": student.age,
        "course": student.course
    }

    students.append(new_student)

    return {
        "message": "Student created successfully",
        "student": new_student
    }


# READ ALL
@app.get("/students")
def get_students():

    return students


# READ ONE
@app.get("/students/{student_id}")
def get_student(student_id: int):

    for student in students:

        if student["id"] == student_id:
            return student

    return {
        "message": "Student not found"
    }


# Update/put
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):

    for item in students:

        if item["id"] == student_id:

            item["name"] = student.name
            item["age"] = student.age
            item["course"] = student.course

            return {
                "message": "Student updated successfully",
                "student": item
            }

    return {
        "message": "Student not found"
    }


# del
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            return {
                "message": "Student deleted successfully"
            }

    return {
        "message": "Student not found"
    }