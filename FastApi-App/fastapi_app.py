from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Student API",
    description="A simple API to manage students",
    version="1.0.0"
)

# Define a Pydantic model for Student
class Student(BaseModel):
    id: int
    name: str
    age: int

@app.get("/ping", tags=["Health Check"], summary="Ping the API", description="Simple health check to see if the API is alive")
def ping():
    return {"message": "pong"}

@app.get(
    "/students/{id}",
    response_model=Student,
    tags=["Students"],
    summary="Get a student by ID",
    description="Fetches a student record by their unique ID"
)
def get_student(id: int):
    return {"id": id, "name": "Dummy Student", "age": 20}
