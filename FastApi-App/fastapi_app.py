from fastapi import FastAPI

app = FastAPI()

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/students/{id}")
def get_student(id: int):
    return {"id": id, "name": "Dummy Student", "age": 20}
