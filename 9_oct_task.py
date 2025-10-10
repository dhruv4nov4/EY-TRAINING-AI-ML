from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowing frontend to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple GET API that returns 5 students
@app.get("/students")
def get_students():
    students = [
        {"id": 1, "name": "Dhruv", "grade": "A"},
        {"id": 2, "name": "Katherine", "grade": "B"},
        {"id": 3, "name": "Damon", "grade": "A"},
        {"id": 4, "name": "Elena", "grade": "C"},
        {"id": 5, "name": "Stefan", "grade": "B"},
    ]
    return {"students": students}