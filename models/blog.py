from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from .user import User

class Blog(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    body: str
    user_id: int | None = Field(default=None, foreign_key="user.id")
    user: "User" = Relationship(back_populates="blogs")