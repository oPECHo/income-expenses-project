import sys
sys.path.insert(0, "/home/nattanon/project/income-expenses-project/server")

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_user():
    user = {
        "username": "tester",
        "email": "tester@gmail.com",
        "password": "password test",
    }
    response = client.post("/register", json=user)
    assert response.status_code == 201
    assert response.json()["username"] == user["username"]
    assert response.json()["email"] == user["email"]

