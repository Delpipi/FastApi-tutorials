from typing import List
from fastapi import APIRouter, status
from sqlmodel import select
from database.session import SessionDep
from repositories.auth import CurrentActiveUserDep
from schemas.user import MainUser, UserCreate, UserPublic
from repositories import user

router = APIRouter(
    prefix='/users', 
    tags=['Users']
)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[UserPublic])
def get_users(session: SessionDep, current_active_user: CurrentActiveUserDep):
    return user.get_users(session)


@router.get('/{id}', status_code=status.HTTP_200_OK, response_model=UserPublic, tags=['Users'])
def get_user(id: int, session: SessionDep, current_active_user: CurrentActiveUserDep): 
    return user.get_user(id,session)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=MainUser, tags=['Users'])
def create_user(request: UserCreate, session: SessionDep):
    return user.create_user(request, session)


@router.patch('/{id}', status_code=status.HTTP_202_ACCEPTED, response_model=UserPublic, tags=['Users'])
def update_user(id: int, request: UserCreate, session: SessionDep, current_active_user: CurrentActiveUserDep):
    return user.update_user(id, request, session)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Users'])
def delete_user(id: int, session: SessionDep, current_active_user: CurrentActiveUserDep):
    user.delete_user(id,session)