from typing import List
from fastapi import APIRouter, status
from sqlmodel import select
from core.oauth2 import RequestForm
from database.session import SessionDep
from repositories import auth
from schemas.user import MainUser

router = APIRouter(
    tags=['Authentication']
)

@router.post('/login', status_code=status.HTTP_200_OK)
def login_for_access_token(form_data: RequestForm,  session: SessionDep):
    return auth.login(form_data,session)