from fastapi import FastAPI

from stock_backend.schemes import (
    MessageScheme,
    UserDBScheme,
    UserPublicScheme,
    UserScheme,
)

app = FastAPI()

db = []


@app.get('/', status_code=200, response_model=MessageScheme)
def read_root():
    return {'text': 'The quick fox jump over the lazy dog.'}


@app.post('/user/', status_code=201, response_model=UserPublicScheme)
def create_user(user: UserScheme):
    user_with_id = UserDBScheme(**user.model_dump(), id=len(db) + 1)
    db.append(user_with_id)

    return user_with_id

    # Automatic cast
    # userForResponse = UserPublicScheme(
    #     **user_with_id.model_dump(exclude={'password'})
    # )
    # return userForResponse
