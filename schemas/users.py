from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_admin: int = 0

    class Config:
        orm_mode = True