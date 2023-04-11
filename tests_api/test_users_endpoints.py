import random
import requests
from src.json_data import Json
from pytest_voluptuous import S

url = 'https://reqres.in/api/users'
params = {'page': {random.randint(1, 9)}, 'per_page': {random.randint(1, 9)}}
user_url = url + f'/{random.randint(1, 9)}'
delayed_response = url + '?delay=3'


def test_get_users_list():
    """Fetches a user list with number of page and quality per page."""
    response = requests.get(url, params=params)
    data = response.json()
    assert response.status_code == 200, f'Expected 200 status, got {response.status_code} instead'
    assert len(data['data']) > 0, f'{data} is empty'
    assert S(Json.list_user_schema) == response.json()


def test_get_user_by_id():
    """Fetches a user by stated id."""
    response = requests.get(user_url)
    assert response.status_code == 200, f'Expected 200 status, got {response.status_code} instead'
    assert S(Json.single_user_schema) == response.json(), f'Expected {Json.single_user_schema}, got {response.json()}' \
                                                          f' instead '


def test_update_user_put():
    """Updates a user info / PUT method."""
    response = requests.put(user_url, data=Json.update_user)
    assert response.status_code == 200, f'Expected 200 status, got {response.status_code} instead'
    assert S(Json.update_user_schema) == response.json(), f'Expected {Json.update_user_schema}, got {response.json()}' \
                                                          f' instead '


def test_update_user_patch():
    """Updates a user info / PATCH method."""
    response = requests.patch(user_url, data=Json.update_user)
    assert response.status_code == 200, f'Expected 200 status, got {response.status_code} instead'
    assert S(Json.update_user_schema) == response.json(), f'Expected {Json.update_user_schema}, got {response.json()}' \
                                                          f' instead '


def test_delete_user():
    """Deletes a user."""
    response = requests.delete(user_url)
    assert response.status_code == 204, f'Expected 204 status, got {response.status_code} instead'


def test_delayed_response():
    """Checks delayed response result."""
    response = requests.get(delayed_response)
    assert response.status_code == 200, f'Expected 200 status, got {response.status_code} instead'
