from sqlalchemy import select

from stock_backend.models import User


def test_create_user(db_session):
    new_user = User(
        username='Alcides', password='123', email='alcides@ribeiro.com'
    )

    db_session.add(new_user)
    db_session.commit()

    user = db_session.scalar(select(User).where(User.username == 'Alcides'))

    assert user.username == 'Alcides'
