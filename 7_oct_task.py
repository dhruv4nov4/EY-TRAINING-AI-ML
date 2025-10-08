@app.get("/employees/average-salary")
def average_salary():
    if not employees:
        return {"average_salary": 0}
    avg = sum(emp["salary"] for emp in employees) / len(employees)
    return {"average_salary": round(avg, 2)}

@app.get("/employees/search")
def search_employees(department: str):
    results = [emp for emp in employees if emp["department"].lower() == department.lower()]
    if not results:
        raise HTTPException(status_code=404, detail="No employees found in this department")
    return results

from typing import Optional

class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    department: Optional[str] = None
    salary: Optional[float] = None

@app.patch("/employees/{emp_id}")
def partial_update(emp_id: int, update_data: EmployeeUpdate):
    for emp in employees:
        if emp["id"] == emp_id:
            if update_data.name is not None:
                emp["name"] = update_data.name
            if update_data.department is not None:
                emp["department"] = update_data.department
            if update_data.salary is not None:
                emp["salary"] = update_data.salary
            return {"message": "Employee partially updated", "employee": emp}
    raise HTTPException(status_code=404, detail="Employee not found")

for emp in employees:
    if emp["name"].lower() == employee.name.lower():
        raise HTTPException(status_code=400, detail="Employee name already exists")

@app.get("/employees")
def get_all_employees(sort_by: str | None = None):
    if sort_by == "salary":
        return sorted(employees, key=lambda x: x["salary"])
    elif sort_by == "name":
        return sorted(employees, key=lambda x: x["name"])
    return employees

