from fastapi import FastAPI
from employee_actions import EmployeeService

app = FastAPI()

def get_employee_service():
    return EmployeeService()

@app.get("/")
def home():
    return {"message": "Welcome to the Employee Service API, please use the /employees endpoint to manage employees."}

@app.get("/employees")
def get_all_employee():
    return get_employee_service().get_all_employee()

@app.get("/employees/{id}")
def get_employee(id: str):
    try:
        return get_employee_service().get_employee(id)
    except ValueError as e:
        return {"error": str(e)}

@app.post("/employees")
def create_employee(name: str, role: str):
    try:
        return get_employee_service().create_employee(name, role)
    except ValueError as e:
        return {"error": str(e)}

@app.put("/employees/{id}")
def update_employee(id: str, name: str, role: str):
    try:
        return get_employee_service().update_employee(id, name, role)
    except ValueError as e:
        return {"error": str(e)}

@app.delete("/employees/{id}")
def delete_employee(id: str):
    try:
        get_employee_service().delete_employee(id)
    except ValueError as e:
        return {"error": str(e)}
    return {"message": f"Employee with ID {id} deleted successfully"}


