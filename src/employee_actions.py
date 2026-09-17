from employee_dao import EmployeeDAO

class EmployeeService:
    def __init__(self, employee_dao:EmployeeDAO=None):
        self.employee_dao = employee_dao or EmployeeDAO()

    def create_employee(self, name:str, role:str):
        return self.employee_dao.add_employee(name, role)

    def get_all_employee(self):
        return self.employee_dao.get_all_employee()

    def get_employee(self, id:str):
        return self.employee_dao.get_employee(id)

    def update_employee(self, id:int, name:str, role:str):
        employee = self.employee_dao.get_employee(id)
        employee.name = name
        employee.role = role
        return self.employee_dao.update_employee(employee)

    def delete_employee(self, id:str):
            self.employee_dao.delete_employee(id)