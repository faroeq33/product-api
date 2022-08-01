import requests


def test_create_products():
    baseurl = "http://localhost:8000"
    product = {
        "brand": "Lunatics",
        "name": "Mempalam",
        "price": 25.00
    }

    response = requests.post(f"{baseurl}/create/product/", json=product, headers={
        "Content-Type": "application/json; charset=utf-8"})

    assert response.status_code == 200
