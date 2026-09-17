
def test_create_and_get_employee(client):
    # Create
    create_response = client.post(
        "/employees",
        params={
            "name": "Integration Test User",
            "role": "QA Engineer"
        }
    )

    assert create_response.status_code == 200

    created_employee = create_response.json()

    # Get all
    get_response = client.get("/employees")

    assert get_response.status_code == 200

    employees = get_response.json()

    # Verify created employee exists
    assert created_employee in employees


def test_get_employee_by_id(client):
    # Create an employee first
    create_response = client.post(
        "/employees",
        params={
            "name": "Integration Test User 2",
            "role": "Backend Developer"
        }
    )

    assert create_response.status_code == 200

    created_employee = create_response.json()
    employee_id = created_employee["id"]

    # Get by ID
    get_response = client.get(f"/employees/{employee_id}")

    assert get_response.status_code == 200

    fetched_employee = get_response.json()

    # Verify fetched employee matches created employee
    assert fetched_employee == created_employee