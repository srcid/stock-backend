from fastapi.testclient import TestClient

from stock_backend.main import app


def test_root_path_should_return_status_200_and_hello_world():
    client = TestClient(app)
    res = client.get('/')

    assert res.status_code == 200
    assert res.json() == {'hello': 'world'}
