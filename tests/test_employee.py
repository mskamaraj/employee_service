from employee import Employee

def test_create_employee():
    employee = Employee(1, "John Doe", "Developer")
    assert employee.id == 1
    assert employee.name == "John Doe"
    assert employee.role == "Developer"