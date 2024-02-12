from fastapi.testclient import TestClient

from stock_backend.main import app


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
