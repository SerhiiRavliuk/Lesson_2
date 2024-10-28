import pytest
import logging
import requests
from requests.auth import HTTPBasicAuth

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
file_handler = logging.FileHandler('test_search.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logging.getLogger().addHandler(file_handler)

@pytest.fixture(scope='class')
def auth():
    session = requests.Session()
    response = session.post('http://127.0.0.1:5002/auth', auth=HTTPBasicAuth('test_user', 'test_pass'))

    if response.status_code != 200:
        pytest.fail("Authentication failed")

    access_token = response.json().get('access_token')
    session.headers.update({'Authorization': 'Bearer ' + access_token})

    yield session

@pytest.mark.parametrize("sort_by, limit, expected_brands", [
    ('price', 5, ["Chevrolet", "Honda", "Mazda", "Kia", "Audi"]),
    ('year', 3, ["Ford", "Honda", "Toyota"]),
    ('engine_volume', 4, ["Honda", "Nissan", "Audi", "BMW"]),
    (None, 2, ["BMW", "Audi"]),
    (None, 0, ["BMW", "Audi", "Mercedes", "Toyota", "Honda"]),
])
def test_get_cars(auth, sort_by, limit, expected_brands):
    logging.info(f"Testing GET /cars with sort_by={sort_by} and limit={limit}")

    params = {}
    if sort_by:
        params['sort_by'] = sort_by
    if limit is not None:
        params['limit'] = limit

    logging.info("Sending GET request to /cars")
    response = auth.get('http://127.0.0.1:5002/cars', params=params)

    assert response.status_code == 200
    cars = response.json()

    actual_brands = [car['brand'] for car in cars]

    assert actual_brands[:len(expected_brands)] == expected_brands
    logging.info("Test passed successfully")
