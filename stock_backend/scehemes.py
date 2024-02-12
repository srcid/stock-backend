from pydantic import BaseModel


class MessageScheme(BaseModel):
    text: str
