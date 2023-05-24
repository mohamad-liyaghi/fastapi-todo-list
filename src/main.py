import uvicorn
from fastapi import FastAPI
from core.config import config

app = FastAPI(
    title='FastApi Todo List',
    description='A TodoList written with FastApi',
    version='1.0.0',
    docs_url='/' 
)

if __name__ == "__main__":
    uvicorn.run(
        host="0.0.0.0",
        app='main:app',
        reload=True if config.ENVIRONMENT != "production" else False,
)