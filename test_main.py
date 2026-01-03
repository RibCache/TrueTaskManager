from fastapi.testclient import TestClient
from main import app
import pytest

client = TestClient(app)

TEST_TASK = {
    "title": "buy coffee",
    "description": "cappuccino"
}


def test_register_user():
    import random
    email = f"Gordon{random.randint(1, 100000)}@piedpiper.com"
    
    response = client.post("/auth/register", json={
        "email": email,
        "password": "qwerty",
        "is_active": True,
        "is_superuser": False,
        "username": "Gordon"
    })
    
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == email
    assert "id" in data
    
def test_create_task():
    response = client.post("/tasks/", json=TEST_TASK)
    
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == TEST_TASK["title"]
    assert data["is_completed"] is False
    assert "id" in data
    
    return data["id"]

def test_get_all_tasks():
    client.post("/tasks/", json=TEST_TASK)
    
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.json()
    
    assert isinstance(data, list)
    assert len(data) > 0
    
def test_task_lifecycle():
    create_resp = client.post("/tasks/", json={"title": "Temporary Task"})
    task_id = create_resp.json()["id"]
    
    new_title = "Updated Title"
    update_resp = client.patch(f"/tasks/{task_id}", json={
        "title": new_title,
        "is_completed": True
    })
    
    assert update_resp.status_code == 200
    assert update_resp.json()["title"] == new_title
    assert update_resp.json()["is_completed"] is True
    
    get_resp = client.get(f"/tasks/{task_id}")
    assert get_resp.json()["title"] == new_title
    
    del_resp = client.delete(f"/tasks/{task_id}")
    assert del_resp.status_code == 204
    
    check_resp = client.get(f"/tasks/{task_id}")
    assert check_resp.status_code == 404