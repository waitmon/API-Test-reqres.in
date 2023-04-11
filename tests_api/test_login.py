import requests
from pytest_voluptuous import S

from src.json_data import Json

url = 'https://reqres.in/api/login'


def test_valid_login():
    """Creates a session."""
    response = requests.post(url, data=Json.valid_user)
    data = response.json()
    assert response.status_code == 200, f'Expected 200 status, got {response.status_code} instead'
    assert data['token'] == 'QpwL5tke4Pnpja7X4', 'Invalid token received'
    assert S(Json.login_schema) == data, f'Expected {S(Json.login_schema)}, got {data} instead'


def test_invalid_user_login():
    """Invalid login data attempt / Checks that response is 400."""
    response = requests.post(url, data=Json.invalid_user)
    data = response.json()
    assert response.status_code == 400, f'Expected 400 status, got {response.status_code} instead'
    assert 'user not found' in data['error'], f'Error in {data["error"]} is different from what is expected.'


def test_invalid_login_password():
    """Invalid login data attempt / Checks that response is 400."""
    response = requests.post(url, data=Json.invalid_login_no_password)
    data = response.json()
    assert response.status_code == 400, f'Expected 400 status, got {response.status_code} instead'
    assert 'Missing password' in data['error'], f'Error in {data["error"]} is different from what is expected.'


def test_invalid_login_email():
    """Invalid login data attempt / Checks that response is 400."""
    response = requests.post(url, data=Json.invalid_login_no_email)
    data = response.json()
    assert response.status_code == 400, f'Expected 400 status, got {response.status_code} instead'
    assert 'Missing email or username' in data['error'], f'Error in {data["error"]} is different from what is expected.'
