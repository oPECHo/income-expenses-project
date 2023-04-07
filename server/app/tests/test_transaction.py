import sys
sys.path.insert(0, "/home/nattanon/project/income-expenses-project/server")

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)
access_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0ZXJAZ21haWwuY29tIiwiZXhwIjoxNjgwODUyNTU0fQ.5-mmlCyvOm_updVZbI34G1QglO4xlxPbkdRIm4nGm0E"

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

def test_update_transaction():
    headers = {"Authorization": f"Bearer {access_token}"}
    transaction = {
        "date": "2023-04-07",
        "body": "update transaction",
        "amount": 100.0,
        "tag": "update test",
        "transaction_type": "expenses",
    }
    response = client.put("/transaction/2", headers=headers, json=transaction)
    assert response.status_code == 202
    assert b"update" in response.content

def test_delete_transaction():
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.delete("/transaction/13", headers=headers)
    if response.status_code == 204:
        print("Done") 
    elif response.status_code == 404:
        print("Not found")