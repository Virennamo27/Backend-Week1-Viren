from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

# Step 1: Initialize the FastAPI app with metadata
app = FastAPI(
    title="Student Management API",
    description="An API to manage student records with ID, name, age, and department",
    version="1.0.0"
)

# Step 2: Define a Pydantic model for a student
class Student(BaseModel):
    id: int
    name: str
    age: int
    dept: str

# Step 3: Hardcoded data in a Python list (temporary "database")
students_db = [
    {"id": 1, "name": "Alice Johnson", "age": 21, "dept": "Computer Science"},
    {"id": 2, "name": "Bob Williams", "age": 22, "dept": "Electrical Engineering"},
    {"id": 3, "name": "Charlie Brown", "age": 20, "dept": "Mechanical Engineering"},
    {"id": 4, "name": "Diana Miller", "age": 23, "dept": "Civil Engineering"},
]

# Step 4: Implement the /students GET endpoint
@app.get(
    "/students",
    response_model=List[Student],
    tags=["Students"],
    summary="Get all students",
    description="Fetches the complete list of students from the database."
)
def get_all_students():
    return students_db

# Step 5: Implement the /students/{id} GET endpoint
@app.get(
    "/students/{id}",
    response_model=Student,
    tags=["Students"],
    summary="Get a student by ID",
    description="Fetches the details of a student by their unique ID."
)
def get_student_by_id(id: int):
    for student in students_db:
        if student["id"] == id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")
