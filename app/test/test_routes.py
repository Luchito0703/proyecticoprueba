# tests/test_routes.py
import pytest
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_add_client():
    resp = client.post("/clients", json={"name": "Alice"})
    assert resp.status_code == 200
    assert "client_id" in resp.json()

def test_add_product_and_sale():
    pr = client.post("/products", json={"name": "Item", "price": 9.99})
    pid = pr.json()["product_id"]
    cr = client.post("/clients", json={"name": "Bob"})
    cid = cr.json()["client_id"]
    sr = client.post("/sales", json={"client_id": cid, "product_id": pid, "quantity": 2})
    assert sr.status_code == 200
    assert sr.json()["message"] == "Sale recorded"
