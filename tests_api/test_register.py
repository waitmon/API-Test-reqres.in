import requests
from src.json_data import Json
from pytest_voluptuous import S

url = 'https://reqres.in/api/register'


def test_valid_registration():
    """Creates a user."""
    response = requests.post(url, data=Json.valid_user)
    data = response.json()
    assert response.status_code == 200, f'Expected 200 status, got {response.status_code} instead'
    assert data['token'] == 'QpwL5tke4Pnpja7X4'
    assert S(Json.register_user_schema) == data, f'Expected {S(Json.register_user_schema)}, got {data} instead'


def test_invalid_registration():
    """Checks that response is 400."""
    response = requests.post(url, data=Json.invalid_user)
    data = response.json()
    error_msg = 'Note: Only defined users succeed registration'
    assert response.status_code == 400, f'Expected 400 status, got {response.status_code} instead'
    assert error_msg in data['error'], f'{error_msg} not in {data["error"]}'
