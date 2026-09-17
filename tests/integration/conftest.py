import os

import pytest
from fastapi.testclient import TestClient

from main import app, get_employee_service
from employee_actions import EmployeeService
from employee_dao import EmployeeDAO


TEST_DB = "employee_test.db"


@pytest.fixture
def client():
    # Create DAO using test database
    test_dao = EmployeeDAO(TEST_DB)

    # Create service using test DAO
    test_service = EmployeeService(test_dao)

    # Override FastAPI dependency
    app.dependency_overrides[get_employee_service] = lambda: test_service

    # Create test client
    with TestClient(app) as test_client:
        yield test_client

    # Cleanup
    app.dependency_overrides.clear()
    test_dao.close()

    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)