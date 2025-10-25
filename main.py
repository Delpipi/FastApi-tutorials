from fastapi import FastAPI
from database.session import SQLModel, engine
from routers import auth, user, blog

SQLModel.metadata.create_all(engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(blog.router)
app.include_router(user.router)

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)