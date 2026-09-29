from fastapi import FastAPI
from employee_actions import EmployeeService
import logging

logging.basicConfig(
    level=logging.INFO, 
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
app = FastAPI()

def get_employee_service():
    return EmployeeService()

@app.get("/")
def home():
    logger.info("Home endpoint called")
    return {"message": "Welcome to the Employee Service API, please use the /employees endpoint to manage employees."}

@app.get("/health")
def health_check():
    logger.info("Health check endpoint called")
    return {"status": "healthy"}

@app.get("/employees")
def get_all_employee():
    logger.info("Fetching all employees")
    return get_employee_service().get_all_employee()

@app.get("/employees/{id}")
def get_employee(id: str):
    try:
        logger.info(f"Fetching employee with ID: {id}")
        return get_employee_service().get_employee(id)
    except ValueError as e:
        return {"error": str(e)}

@app.post("/employees")
def create_employee(name: str, role: str):
    try:
        logger.info(f"Creating employee: {name}, Role: {role}")
        return get_employee_service().create_employee(name, role)
    except ValueError as e:
        return {"error": str(e)}

@app.put("/employees/{id}")
def update_employee(id: str, name: str, role: str):
    try:
        logger.info(f"Updating employee with ID: {id}")
        return get_employee_service().update_employee(id, name, role)
    except ValueError as e:
        return {"error": str(e)}

@app.delete("/employees/{id}")
def delete_employee(id: str):
    try:
        logger.info(f"Deleting employee with ID: {id}")
        get_employee_service().delete_employee(id)
    except ValueError as e:
        return {"error": str(e)}
    return {"message": f"Employee with ID {id} deleted successfully"}


