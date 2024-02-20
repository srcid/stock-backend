from fastapi.testclient import TestClient

from stock_backend.main import app
from stock_backend.schemes import UserPublicScheme, UserScheme


def test_root_path_should_return_status_200_and_hello_world(client):
    res = client.get('/')

    assert res.status_code == 200
    assert res.json() == {'text': 'The quick fox jump over the lazy dog.'}


def test_create_user(client):
    res = client.post(
        '/user/',
        json={
            'username': 'Tsujiro Kymimame',
            'email': 'tsju@mail.com',
            'password': '123',
        },
    )

    assert res.status_code == 201
    assert res.json() == {
        'username': 'Tsujiro Kymimame',
        'email': 'tsju@mail.com',
        'id': 1,
    }


def test_read_all_users_empty_table(client):
    res = client.get('/user/')
    assert res.status_code == 200
    assert res.json() == {'users': []}


def test_read_all_users_with_one_user(client, user):
    user_public_dict = UserPublicScheme.model_validate(user).model_dump()
    res = client.get('/user/')

    assert res.status_code == 200
    assert res.json() == {'users': [user_public_dict]}


def test_update_user(client, user):
    altered_user_dict = {
        'username': 'Jalin Habbei Bin Said',
        'email': 'jalin@gmail.com',
        'password': 'jooj',
    }

    res = client.put(f'/user/{user.id}', json=altered_user_dict)

    assert res.status_code == 200
    assert res.json() == {
        'id': user.id,
        'username': altered_user_dict['username'],
        'email': altered_user_dict['email'],
    }


def test_update_user_with_non_existing_id(client, user):
    altered_user_dict = {
        'username': 'Jalin Habbei Bin Said',
        'email': 'jalin@gmail.com',
        'password': 'jooj',
    }

    res = client.put(f'/user/99999', json=altered_user_dict)

    assert res.status_code == 404
