import requests
from pytest_voluptuous import S
from src.json_data import Json

url_list_resources = 'https://reqres.in/api/unknown'
url_resource_id = 'https://reqres.in/api/{resource}/4'
url_invalid_resource = 'https://reqres.in/api/unknown/23'


def test_get_resources():
    """Fetches a resource list."""
    response = requests.get(url_list_resources)
    data = response.json()
    assert response.status_code == 200, f'Expected 200 status, got {response.status_code} instead'
    assert len(data['data']) > 0, f'{data} is empty'
    assert S(Json.list_resource_schema) == data, f'Expected {S(Json.list_resource_schema)}, got {data} instead'


def test_get_resource_id():
    """Fetches an unknown resource by id."""
    response = requests.get(url_resource_id)
    data = response.json()
    assert response.status_code == 200, f'Expected 200 status, got {response.status_code} instead'
    assert len(data['data']) > 0, f'{data} is empty'
    assert S(Json.single_resource_schema) == data, f'Expected {S(Json.single_resource_schema)}, got {data} instead'


def test_update_resource_put():
    """Updates an unknown resource / PUT method."""
    response = requests.put(url_resource_id)
    data = response.json()
    assert response.status_code == 200, f'Expected 200 status, got {response.status_code} instead'
    assert 'updatedAt' in data, 'No updated information in response body'


def test_update_resource_patch():
    """Updates an unknown resource / PATCH method."""
    response = requests.patch(url_resource_id)
    data = response.json()
    assert response.status_code == 200, f'Expected 200 status, got {response.status_code} instead'
    assert 'updatedAt' in data, 'No updated information in response body'


def test_delete_resource():
    """Delete an unknown resource."""
    response = requests.delete(url_resource_id)
    assert response.status_code == 204, f'Expected 204 status, got {response.status_code} instead'


def test_single_resource_not_found():
    """Checks non-existing resource returns 404 status code."""
    response = requests.get(url_invalid_resource)
    assert response.status_code == 404, f'Expected 404 status, got {response.status_code} instead'
    assert response.json() == {}, f'Expected json is not empty'
