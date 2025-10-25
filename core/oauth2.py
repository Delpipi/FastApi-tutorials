from typing import Annotated
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

TokenDep = Annotated[str, Depends(oauth2_scheme)]

RequestForm = Annotated[OAuth2PasswordRequestForm, Depends()]