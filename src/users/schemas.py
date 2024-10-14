import uuid as uuid_pkg
from pydantic import BaseModel, Field


class UserCreate(BaseModel):
    email: str
    password: str = Field(min_length=7, max_length=32)


class User(UserCreate):
    uuid: uuid_pkg.UUID
    first_name: str
    last_name: str | None = None
    role_id: int


class UserRole(BaseModel):
    id: int
    title: str