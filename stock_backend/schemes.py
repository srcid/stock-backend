from pydantic import BaseModel, ConfigDict, EmailStr


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
    model_config = ConfigDict(from_attributes=True)


class UserPublicListScheme(BaseModel):
    users: list[UserPublicScheme]
