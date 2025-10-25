from typing import List
from fastapi import APIRouter, HTTPException, status
from pwdlib import PasswordHash
from sqlmodel import select
from database.session import SessionDep
from models.user import User
from schemas.user import MainUser, UserCreate, UserPublic

password_hash = PasswordHash.recommended()

def verify_password(plain_password, hashed_password):
    return password_hash.verify(plain_password, hashed_password)

def get_password_hash(password):
    return password_hash.hash(password=password)


def get_users(session: SessionDep):
    users = session.exec(select(User)).all()
    return users


def get_user(id: int, session: SessionDep): 
    user = session.get(User, id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    return user

def create_user(request: UserCreate, session: SessionDep):
    new_user = User(name=request.name, email=request.email, password=get_password_hash(request.password), disabled=True)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


def update_user(id: int, request: UserCreate, session: SessionDep):
    user_db = session.get(User, id)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    user_data = request.model_dump(exclude_unset=True)
    user_db.sqlmodel_update(user_data)
    session.add(user_db)
    session.commit()
    session.refresh(user_db)
    return user_db


def delete_user(id: int, session: SessionDep):
    user = session.get(User, id)
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')
    session.delete(user)
    session.commit()