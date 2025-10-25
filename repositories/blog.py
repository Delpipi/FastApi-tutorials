from fastapi import HTTPException,status
from sqlmodel import select
from database.session import SessionDep
from models.blog import Blog
from schemas.blog import MainBlog

def get_blogs(session: SessionDep):
    blogs = session.exec(select(Blog)).all()
    return blogs


def get_blog(id: int, session: SessionDep):
    blog = session.get(Blog, id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Blog not found')
    return blog


def create_blog(request: MainBlog, session: SessionDep):
    new_blog = Blog(title=request.title, body=request.body, user_id= 1)
    session.add(new_blog)
    session.commit()
    session.refresh(new_blog)
    return new_blog


def update_blog(id: int, request: MainBlog, session: SessionDep):
    blog_db = session.get(Blog, id)
    if not blog_db:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Blog not found')
    blog_data = request.model_dump(exclude_unset=True)
    blog_db.sqlmodel_update(blog_data)
    session.add(blog_db)
    session.commit()
    session.refresh(blog_db)
    return blog_db


def delete_blog(id: int, session: SessionDep):
    blog = session.get(Blog, id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Blog not found')
    session.delete(blog)
    session.commit()