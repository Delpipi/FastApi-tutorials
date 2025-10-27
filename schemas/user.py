from typing import List
from pydantic import BaseModel
from .blog import MainBlog

class MainUser(BaseModel):
    id: int
    name: str
    email: str
    disabled: bool

class UserCreate(MainUser):
    password: str

class UserPublic(MainUser):
    blogs: List[MainBlog]