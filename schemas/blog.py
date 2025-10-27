from pydantic import BaseModel

class MainBlog(BaseModel):
    id: int
    title: str
    body: str

class BlogPublic(MainBlog):
    user_id: int