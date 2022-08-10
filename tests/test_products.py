import requests
import pytest

from tests.helpers.testdatahelper import insert_test_data


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


def test_get_products():
    # TODO : test if products are inserted
    # insert_test_data()

    baseurl = "http://localhost:8000"
    response = requests.get(f"{baseurl}/products/", headers={
        "Content-Type": "application/json; charset=utf-8"})

    assert response.status_code == 200
