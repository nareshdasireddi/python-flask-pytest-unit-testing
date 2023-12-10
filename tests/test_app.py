# test_app.py

import json
import pytest
from app import app

# Fixture setup for the Flask test client
# This fixture is used by all the test cases
@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        # Note: The setup code will be executed before each test case
        print("\nSetup for client")
        # Create a task for testing
        yield client
        # Note: The teardown code will be executed after each test case
        print("\nTeardown for client")

# Test case for getting tasks
def test_get_tasks(client):
    # Arrange: No additional setup required
    print("Running test_get_tasks")
    # Act: Make a request to the /tasks endpoint
    response = client.get('/tasks')
    # Assert: Check the response status code and content
    assert response.status_code == 200
    assert 'tasks' in json.loads(response.data)
    # Comment: Ensure that the 'tasks' key is present in the response data

# Test case for creating a task
def test_create_task(client):
    print("Running test_create_task")
    # Arrange: Prepare data for creating a task
    data = {'title': 'Test Task'}

    # Act: Make a POST request to the /tasks endpoint with the data
    response = client.post('/tasks', json=data)

    # Assert: Check the response status code and content
    assert response.status_code == 201
    assert 'task' in json.loads(response.data)
    assert json.loads(response.data)['task']['title'] == 'Test Task'
    assert json.loads(response.data)['task']['id'] == 1
    # Comment: Ensure that the 'task' key is present in the response data

# Test case for updating a task
def test_update_task(client):
    print("Running test_update_task")
    # Arrange: Prepare data for updating a task
    data = {'title': 'Updated Task'}

    # Act: Make a PUT request to the /tasks/1 endpoint with the data
    response = client.put('/tasks/1', json=data)

    # Assert: Check the response status code and content
    assert response.status_code == 200
    assert 'task' in json.loads(response.data)
    assert json.loads(response.data)['task']['title'] == 'Updated Task'
    # Comment: Ensure that the task title is updated correctly

# Test case for deleting a task
def test_delete_task(client):
    print("Running test_delete_task")
    # Arrange: No additional setup required

    # Act: Make a DELETE request to the /tasks/1 endpoint
    response = client.delete('/tasks/1')

    # Assert: Check the response status code and content
    assert response.status_code == 200
    assert 'result' in json.loads(response.data)
    assert json.loads(response.data)['result'] is True
    assert len(json.loads(client.get('/tasks').data)['tasks']) == 0
    # Comment: Ensure that the deletion result is True

# Test case for a non-existing task
def test_task_not_found(client):
    print("Running test_task_not_found")
    # Arrange: No additional setup required

    # Act: Make a request to a non-existing task endpoint
    response = client.get('/tasks/99')

    # Assert: Check the response status code and content
    assert response.status_code == 404
    assert 'error' in json.loads(response.data)
    assert json.loads(response.data)['error'] == 'Task not found'
    # Comment: Ensure that a proper error response is returned for a non-existing task
