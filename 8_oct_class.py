from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app=FastAPI()

class Employee(BaseModel):
    id:int
    name:str
    department:str
    salary:float

employees=[
    {"id":1,"name":"Aarav","department":"HR","salary":550000}
]

@app.get("/employees")
def get_all():
    return employees

@app.post("/employees",status_code=201)
def add_employee(employee:Employee):
    employees.append(employee.dict())
    return employee

@app.get("/employees/{emp_id}")
def get_employee(emp_id:int):
    for emp in employees:
        if emp["id"]==emp_id:
            return emp
    raise HTTPException(status_code=404, detail="Employee Not Found")

#--put---
@app.put("/employees/{emp_id}")
def updated_employee(emp_id:int, updated_employee: Employee):
    for i,emp in enumerate(employees):
        if emp["id"] == emp_id:
            employees[i]=updated_employee.dict()
            return {"message":"employee updated","employee":updated_employee}
        raise HTTPException(status_code=404,detail="employee not found")

#---DELETE---
@app.delete("/employees/{emp_id}")
def delete_employee(emp_id:int):
    for i, emp in enumerate(employees):
        if emp["id"]==emp_id:
            deleted_employee=employees.pop(i)
            return {
                "message":f"Employee with ID{emp_id} deleted successfully",
                "deleted_employee": deleted_employee
            }
    raise HTTPException(status_code=404,detail=f"employee with ID {emp_id} not found")

from fastapi.testclient import TestClient
from main import app

client=TestClient(app)

#----test 1----
def test_get_all_emp():
    response = client.get("/employees") #ACT
    assert response.status_code==200 #assert
    assert isinstance(response.json(),list)#assert

#---- test 2 ----
def test_add_emp():
    new_emp = {
        "id":2,
        "name":"Neha Verma",
        "department":"IT",
        "salary":50000
    }
    response = client.post("/employees",json=new_emp)
    assert response.status_code==201
    assert response.json()["name"]=="Neha Verma"

#----test 3----
def test_get_emo_by_id():
    response = client.get("/employees/1")
    assert response.status_code == 200
    assert response.json()["name"] == "Aarav"

#----test 4----
def test_get_emp_not_found():
    response = client.get("/employees/999")
    assert response.status_code == 404
    assert response.json()["detail"] == "Employee Not Found"

#---test 5 - put -----
def test_update_emp():
    new_emp={
        "id": 2,
        "name": "Riya",
        "department": "IT",
        "salary": 50000
    }
    response = client.post("/employees", json=new_emp)

    updated_emp={
        "id":2,
        "name":"Aashi",
        "department":"IT",
        "salary":60000
    }
    response = client.put("/employees/2",json=updated_emp)
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Employee updated successfully"
    assert data["name"] == "Aashi"
    assert data["salary"] == 60000