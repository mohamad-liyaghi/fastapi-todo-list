import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import config
from api import router
from core.middlewares import AuthBackend, AuthenticationMiddleware

app = FastAPI(
    title='FastApi Todo List',
    description='A TodoList written with FastApi',
    version='1.0.0',
    docs_url='/'
)

# Include all routers
app.include_router(router)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add authentication middleware
app.add_middleware(
    AuthenticationMiddleware,
    backend=AuthBackend(),
)

if __name__ == "__main__":
    uvicorn.run(
        host="0.0.0.0",
        app='main:app',
        reload=True if config.ENVIRONMENT != "production" else False,
    )
