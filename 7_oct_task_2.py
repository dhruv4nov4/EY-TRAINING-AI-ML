from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
app=FastAPI()
class Employee(BaseModel):
    id:int
    name:str
    department:str
    salary:float

employees=[
    {"id":1,"name":"Aarav","department":"HR","salary":550000},
    {"id":2,"name":"Ashish","department":"Finance","salary":750000},
    {"id":3,"name":"Charvi","department":"Tech","salary":90000},
    {"id":4,"name":"Ruchi","department":"Audit","salary":750000}
]

#--------GET----------
@app.get("/employees")
def get_all_employees():
    return {"employees": employees}

@app.get("/employees/{employees_id}")
def get_employees(employees_id:int):
    for e in employees:
        if e["id"]==employees_id:
            return e
    raise HTTPException(status_code=404, detail="employee not found")

#-----POST----
@app.post("/employees",status_code=201)
def add_employee(employee: Employee):
    employees.append(employee.dict())
    return{"message":"Employees added successfully","employee":employee}

#--put---
@app.put("/employees/{employees_id}")
def updated_employee(employees_id:int, updated_employee: Employee):
    for i,e in enumerate(employees):
        if e["id"] == employees_id:
            employees[i]=updated_employee.dict()
            return {"message":"employee updated","employee":updated_employee}
        raise HTTPException(status_code=404,detail="employee not found")

#---DELETE---
@app.delete("/employees/{employees_id}")
def delete_employee(employees_id:int):
    for i, emp in enumerate(employees):
        if emp["id"]==employees_id:
            deleted_employee=employees.pop(i)
            return {
                "message":f"Employee with ID{employees_id} deleted successfully",
                "deleted_employee": deleted_employee
            }
    raise HTTPException(status_code=404,detail=f"employee with ID {employees_id} not found")

