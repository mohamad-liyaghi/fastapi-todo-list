from fastapi import Depends
from fastapi.routing import APIRouter
from core.factory import Factory
from app.controllers import AuthController
from app.schemas import (
    UserRegisterRequest,
    UserRegisterResponse
)

router = APIRouter()


@router.post("/register", response_model=UserRegisterResponse)
async def register_user(
    request: UserRegisterRequest,
    auth_controller: AuthController = Depends(Factory().get_auth_controller),
) -> UserRegisterResponse:
    user = await auth_controller.register(
        username=request.username,
        password=request.password,
    )
    return user
