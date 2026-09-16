class Employee:
    def __init__(self,id:int, name:str, role:str):
        self.id = id
        self.name = name
        self.role = role

    def __str__(self):
        return f"Employe(id={self.id},name={self.name}, role={self.role})"