from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import Session

from stock_backend.schemes import (
    MessageScheme,
    UserPublicListScheme,
    UserPublicScheme,
    UserScheme,
)
from stock_backend.database import get_session
from stock_backend.models import User


app = FastAPI()


@app.get('/', status_code=200, response_model=MessageScheme)
def read_root():
    return {'text': 'The quick fox jump over the lazy dog.'}


@app.get('/user/', status_code=200, response_model=UserPublicListScheme)
def read_all_users(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):

    users = session.scalars(select(User).offset(skip).limit(limit)).all()

    return {'users': users}


@app.post('/user/', status_code=201, response_model=UserPublicScheme)
def create_user(user: UserScheme, session: Session = Depends(get_session)):
    db_user = session.scalar(
        select(User).where(User.username == user.username)
    )

    if db_user:
        raise HTTPException(status_code=400, detail='Username already exists.')

    db_user = User(
        username=user.username, password=user.password, email=user.email
    )

    session.add(db_user)
    session.commit()

    session.refresh(db_user)
    return db_user


@app.put('/user/{user_id}', status_code=200, response_model=UserPublicScheme)
def update_user(
    user_id: int, user: UserScheme, session: Session = Depends(get_session)
):
    db_user: User = session.scalar(select(User).where(User.id == user_id))

    if not db_user:
        raise HTTPException(status_code=404, detail='User not found')

    db_user.username = user.username
    db_user.email = user.email
    db_user.password = user.password

    session.commit()
    session.refresh(db_user)

    return db_user
