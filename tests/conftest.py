import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from stock_backend.main import app
from stock_backend.models import Base, User
from stock_backend.database import get_session
from stock_backend.schemes import UserScheme


@pytest.fixture
def client(db_session):
    def get_session_override():
        return db_session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client


@pytest.fixture
def db_session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )
    session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)
    yield session()
    Base.metadata.drop_all(engine)


@pytest.fixture
def user(db_session):
    user = User(
        username='Sebastian Herman',
        email='sbshm@servidor.com.jp',
        password='asjla',
    )

    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    return user
