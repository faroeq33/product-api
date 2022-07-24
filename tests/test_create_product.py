import requests


def test_create_products_equals_200():
    baseurl = "http://localhost:5000/api/"
    response = requests.post(f"{baseurl}/create/product/", json={
        "brand": "Lunatics",
        "name": "Mempalam",
        "price": 25.00,
    })
    assert response.status_code == 200


# def test_get_locations_for_us_90210_check_country_equals_united_states():
#     response = requests.get("http://api.zippopotam.us/us/90210")
#     response_body = response.json()
#     assert response_body["country"] == "United States"
