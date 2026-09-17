from employee import Employee
import sqlite3

import employee

class EmployeeDAO:
    def __init__(self, database:str="employee.db"):
        self.connection = sqlite3.connect(database, check_same_thread=False)
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        role TEXT NOT NULL)
        """
        self.connection.execute(query)
        self.connection.commit()

    def add_employee(self, name:str, role:str):
        query = """
        INSERT INTO employees (name, role) VALUES (?, ?)
        """
        cursor = self.connection.execute(query,(name, role))
        self.connection.commit()
        return Employee(cursor.lastrowid, name, role)
       

    def get_employee(self, id:int):
        query = """
        SELECT id, name, role FROM employees WHERE id=?
        """
        cursor = self.connection.execute(query,(id,))
        row = cursor.fetchone()
        if row is None:
            raise ValueError(f"Employee {id} does not exist")

        return Employee(row[0], row[1], row[2])

    def get_all_employee(self):
        query = """
        SELECT id, name, role FROM employees
        """
        cursor = self.connection.execute(query)
        rows = cursor.fetchall()

        employees = []
        for row in rows:
            employees.append(Employee(row[0], row[1], row[2]))
        
        return employees;

    def update_employee(self, employee:Employee):
        query = """
        UPDATE employees SET name=?, role=? WHERE id=?
        """
        cursor = self.connection.execute(query, (employee.name, employee.role, employee.id))
        self.connection.commit()
        
        if cursor.rowcount == 0:
            raise ValueError(f"Employee {employee.id} does not exist")

        return self.get_employee(employee.id)

    def delete_employee(self, id:str):
        query = """
        DELETE FROM employees WHERE id = ?
        """
        cursor = self.connection.execute(query, (id,))
        self.connection.commit()
        if cursor.rowcount == 0:
            raise ValueError(f"Employee {id} does not exist")

    def close(self):
        self.connection.close()

        
