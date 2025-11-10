#configure verbs
from fastapi import FastAPI

app=FastAPI()

#GET
@app.get("/students")
def get_students():
    return {"This is a GET request"}

#POST
@app.post("/students")
def create_students():
    return {"This is a POST request"}

#PUT
@app.put("/students")
def update_student():
    return {"This is a PUT request"}

#DELETE
@app.delete("/students")
def delete_student():
    return {"This is a DELETE request"}

# NEW CONTENT
from fastapi import FastAPI

#create fastapi instance
app=FastAPI()

#root endpoint
@app.get("/")
def read_root():
    return {"message":"Welcome to the FastAPI demo!"}

#path parameter example
@app.get("/students/{student_id}")
def get_student(student_id: int):
    return {"student_id":student_id,"name":"Rahul","course":"AI"}

# NEW CONTENT
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app=FastAPI()

#pydantic model for validation
class Student(BaseModel):
    id:int
    name:str
    age:int
    course:str

students =[
    {"id":1,"name":"Aarav","age":18,"course":"Maths"},
    {"id":2,"name":"Ashish","age":22,"course":"Economics"},
    {"id":3,"name":"Charvi","age":21,"course":"AI"},
    {"id":4,"name":"Ruchi","age":28,"course":"Physics"}
]
#--------GET----------
@app.get("/students")
def get_all_students():
    return {"students": students}

@app.get("/students/{student_id}")
def get_students(student_id:int):
    for s in students:
        if s["id"]==student_id:
            return s
    raise HTTPException(status_code=404, detail="Student not found")


#-----POST----
@app.post("/students",status_code=201)
def add_student(student: Student):
    students.append(student.dict())
    return{"message":"Student added successfully","student":student}

#--put---
@app.put("/students/{student_id}")
def update_student(student_id:int, updated_student: Student):
    for i,s in enumerate(students):
        if s["id"] == student_id:
            student[i]=updated_student.dict()
            return {"message":"Student updated","student":updated_student}
        raise HTTPException(status_code=404,detail="Student not found")

#---delete----