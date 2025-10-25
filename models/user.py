from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .blog import Blog

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    email: str
    password: str
    disabled: bool
    blogs: list["Blog"] = Relationship(back_populates="user")
