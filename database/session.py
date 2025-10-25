from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine
from core.config import DATABASE_URL

connect_args = {"check_same_thread": False}
engine = create_engine(DATABASE_URL, connect_args=connect_args)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]