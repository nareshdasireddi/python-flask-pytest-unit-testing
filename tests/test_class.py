import json
import pytest
from app import app

# Fixture for creating a test client
# This fixture is used by all the test cases
@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    # Note: The setup code will be executed before each test case
    print("\nSetup for client fixture====================")
    yield client
    # Note: The teardown code will be executed after each test case
    print("\nTeardown for client fixture====================")

# Test class for the Task API
class TestTaskAPI:
    # Note: The setup code will be executed before each test case
    @classmethod
    def setup_class(cls):
        print("\nSetup for TestTaskAPI AT CLASS LEVEL")
        # Perform setup tasks if needed for the entire test class
        pass
    # Note: The teardown code will be executed after each test case
    @classmethod
    def teardown_class(cls):
        print("\nTeardown for TestTaskAPI At CLASS LEVEL")
        # Perform teardown tasks if needed for the entire test class
        pass
    # Test case for getting tasks
    def test_get_tasks(self, client):
        print("Running test_get_tasks")
        response = client.get('/tasks')
        assert response.status_code == 200
        assert b'tasks' in response.data
    # Test case for creating a task
    def test_create_task(self, client):
        print("Running test_create_task")
        response = client.post('/tasks', json={'title': 'Test Task'})
        assert response.status_code == 201
        assert b'Test Task' in response.data
    # Test case for getting a task
    def test_get_task(self, client):
        print("Running test_get_task")
        response = client.post('/tasks', json={'title': 'Test Task'})
        task_id = json.loads(response.data)['task']['id']

        response = client.get(f'/tasks/{task_id}')
        assert response.status_code == 200
        assert b'Test Task' in response.data
    # Test case for updating a task
    def test_update_task(self, client):
        print("Running test_update_task")
        response = client.post('/tasks', json={'title': 'Test Task'})
        task_id = json.loads(response.data)['task']['id']

        response = client.put(f'/tasks/{task_id}', json={'title': 'Updated Task'})
        assert response.status_code == 200
        assert b'Updated Task' in response.data
    # Test case for deleting a task
    def test_delete_task(self, client):
        print("Running test_delete_task")
        response = client.post('/tasks', json={'title': 'Test Task'})
        task_id = json.loads(response.data)['task']['id']

        response = client.delete(f'/tasks/{task_id}')
        assert response.status_code == 200
