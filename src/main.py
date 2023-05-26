import uvicorn
from fastapi import FastAPI
from core.config import config
from api import router

app = FastAPI(
    title='FastApi Todo List',
    description='A TodoList written with FastApi',
    version='1.0.0',
    docs_url='/'
)

# Include all routers
app.include_router(router)

if __name__ == "__main__":
    uvicorn.run(
        host="0.0.0.0",
        app='main:app',
        reload=True if config.ENVIRONMENT != "production" else False,
    )
