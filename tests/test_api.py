import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Inventory Management API"

def test_get_inventory(client):
    response = client.get("/inventory")
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)
    assert len(data) >= 1

def test_get_single_item(client):
    response = client.get("/inventory/1")
    assert response.status_code == 200
    data = response.get_json()
    assert data["id"] == 1

def test_invalid_item(client):
    response = client.get("/inventory/999")
    assert response.status_code == 404

def test_create_item(client):
    new_item = {
        "barcode": "123456789",
        "product_name": "Bread",
        "brand": "Sunrise",
        "price": 3.99,
        "stock": 40,
        "category": "Bakery"
    }

    response = client.post(
        "/inventory",
        json=new_item
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["product_name"] == "Bread"

def test_update_item(client):
    updates = {
        "price": 8.50,
        "stock": 100
    }

    response = client.patch(
        "/inventory/1",
        json=updates
    )
    assert response.status_code == 200
    data = response.get_json()
    assert data["price"] == 8.50
    assert data["stock"] == 100

def test_delete_item(client):
    response = client.delete("/inventory/2")
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Item deleted successfully"

def test_search_product(client):
    response = client.get("/search/737628064502")
    assert response.status_code in [200, 404]

def test_import_product(client):
    response = client.post("/import/737628064502")
    assert response.status_code in [201, 404]
