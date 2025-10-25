from typing import List
from fastapi import APIRouter,status
from database.session import SessionDep
from repositories.auth import CurrentActiveUserDep
from schemas.blog import MainBlog, BlogPublic
from repositories import blog

router = APIRouter(
    prefix='/blogs',
    tags=['Blogs']
)

@router.get('/', status_code=status.HTTP_200_OK, response_model=List[BlogPublic])
def get_blogs(session: SessionDep, current_active_user: CurrentActiveUserDep):
    return blog.get_blogs(session)


@router.get('/{id}', status_code=status.HTTP_200_OK,response_model=BlogPublic)
def get_blog(id: int, session: SessionDep, current_active_user: CurrentActiveUserDep):
    return blog.get_blog(id, session)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=BlogPublic, tags=['Blogs'])
def create_blog(request: MainBlog, session: SessionDep, current_active_user: CurrentActiveUserDep):
    return blog.create_blog(request,session)


@router.patch('/{id}', status_code=status.HTTP_200_OK, response_model=BlogPublic, tags=['Blogs'])
def update_blog(id: int, request: MainBlog, session: SessionDep, current_active_user: CurrentActiveUserDep):
   return blog.update_blog(id, request, session)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Blogs'])
def delete_blog(id: int, session: SessionDep, current_active_user: CurrentActiveUserDep):
   blog.delete_blog(id,session)