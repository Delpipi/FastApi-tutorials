from pydantic import BaseModel

class MainBlog(BaseModel):
    title: str
    body: str

class BlogPublic(MainBlog):
    user_id: int