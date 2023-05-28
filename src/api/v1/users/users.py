from fastapi import Depends, status
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from core.factory import Factory
from app.controllers import AuthController
from typing import Annotated
from app.schemas import (
    UserRegisterRequest,
    UserRegisterResponse,
    UserAccessTokenResponse,
)

router = APIRouter()


@router.post(
    "/register",
    response_model=UserRegisterResponse,
    status_code=status.HTTP_201_CREATED,
)
async def register_user(
    request: UserRegisterRequest,
    auth_controller: AuthController = Depends(Factory().get_auth_controller),
) -> UserRegisterResponse:
    user = await auth_controller.register(
        username=request.username,
        password=request.password,
    )
    return user


@router.post('/login', status_code=status.HTTP_200_OK)
async def get_access_token(
    request: Annotated[OAuth2PasswordRequestForm, Depends()],
    auth_controller: AuthController = Depends(Factory().get_auth_controller)
) -> UserAccessTokenResponse:
    access_token = await auth_controller.create_access_token(
        username=request.username, password=request.password
    )
    return {"access_token": access_token, "token_type": "bearer"}
