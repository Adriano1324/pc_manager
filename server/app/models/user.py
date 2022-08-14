from pydantic import BaseModel


class CreateUser(BaseModel):
    username: str
    password: str


class User(CreateUser):
    active: bool = True
