import random
import string
from pytest_voluptuous import S


class Json:
    """Contains payloads for basic https methods and json schema validation tests."""
    # JSON for CRUD requests
    update_user = {
        'name': 'Tony',
        'job': 'waste management business'
    }

    valid_user = {
        "email": "eve.holt@reqres.in",
        "password": 'cityslicka'
    }

    invalid_user = {
        "username": (random.choices(string.ascii_letters.lower(), k=6)),
        "email": (random.choices(string.ascii_letters.lower(), k=6)),
        "password": (random.choices(string.ascii_letters.lower(), k=6))
    }
    invalid_login_no_password = {
        "email": "peter@klaven",
    }
    invalid_login_no_email = {
        "password": 'cityslicka'
    }

    # JSON Schemas for schemas validation tests
    list_user_schema = S({
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": [{
            "id": int,
            "email": str,
            "first_name": str,
            "last_name": str,
            "avatar": str
        },
        ],
        "support":
            {
                "url": str,
                "text": str
            }
    })

    single_user_schema = S({
        "data": {
            "id": int,
            "email": str,
            "first_name": str,
            "last_name": str,
            "avatar": str
        },
        "support": {
            "url": str,
            "text": str
        }
    })

    list_resource_schema = S({
        "page": int,
        "per_page": int,
        "total": int,
        "total_pages": int,
        "data": [{
            "id": int,
            "name": str,
            "year": int,
            "color": str,
            "pantone_value": str
        },
        ],
        "support":
            {
                "url": str,
                "text": str
            }
    })

    single_resource_schema = S({
        "data": {
            "id": int,
            "name": str,
            "year": int,
            "color": str,
            "pantone_value": str
        },
        "support":
            {
                "url": str,
                "text": str
            }
    })

    register_user_schema = S({
        "id": int,
        "token": str,
    })

    update_user_schema = S({
        "name": str,
        "job": str,
        "updatedAt": str
    })

    login_schema = S(
        {
                "token": str
        }
    )
