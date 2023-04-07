import sys
sys.path.insert(0, "/home/nattanon/project/income-expenses-project/server")

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJuYXR0YW5vbjAyODBAZ21haWwuY29tIiwiZXhwIjoxNjgwODUwMjY2fQ.TuD2eNOf4pfKAsUxPfJQOClKFdqGVJlyAM_29jfkNjA"

def test_search_transactions():
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.get("/transaction/",headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_transaction():
    headers = {"Authorization": f"Bearer {access_token}"}
    transaction = {
        "date": "2023-04-07",
        "body": "Test transaction",
        "amount": 100.0,
        "tag": "test",
        "transaction_type": "expenses",
    }
    response = client.post("/transaction/", headers=headers, json=transaction)
    assert response.status_code == 201
    assert response.json()["date"] == transaction["date"]
    assert response.json()["body"] == transaction["body"]
    assert response.json()["amount"] == transaction["amount"]
    assert response.json()["tag"] == transaction["tag"]
    assert response.json()["transaction_type"] == transaction["transaction_type"]

