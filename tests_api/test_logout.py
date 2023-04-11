import requests

url = 'https://reqres.in/api/logout'


def test_valid_logout():
    """Ends a session."""
    response = requests.post(url)
    assert response.status_code == 200, f'Expected 200 status, got {response.status_code} instead'

