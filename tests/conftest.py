import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from stock_backend.main import app
from stock_backend.models import Base


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def db_session():
    engine = create_engine('sqlite:///:memory:')
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield session()
    Base.metadata.drop_all(engine)
