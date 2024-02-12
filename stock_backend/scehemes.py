from pydantic import BaseModel, EmailStr


class MessageScheme(BaseModel):
    text: str


class UserScheme(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublicScheme(BaseModel):
    id: int
    username: str
    email: EmailStr


class UserDBScheme(UserScheme):
    id: int
