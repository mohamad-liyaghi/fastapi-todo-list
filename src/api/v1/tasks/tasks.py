from fastapi import Depends, status
from fastapi.routing import APIRouter
from core.dependencies import AuthenticationRequired
from app.controllers import TaskController
from core.factory import Factory
from app.schemas import (
    TaskCreateRequest,
    TaskCreateResponse,
    TaskUpdateRequest,
    TaskUpdateResponse,
)
from core.dependencies import get_current_user
from uuid import UUID

router = APIRouter(
    dependencies=[Depends(AuthenticationRequired)],
)


@router.post('/create', status_code=status.HTTP_201_CREATED)
async def create_task(
    request: TaskCreateRequest,
    task_controller: TaskController = Depends(Factory().get_task_controller),
    current_user: int = Depends(get_current_user)
) -> TaskCreateResponse:

    task = await task_controller.create(
        title=request.title,
        description=request.description,
        owner_id=current_user.id
    )
    return task


@router.put('/update/{task_uuid}/', status_code=status.HTTP_200_OK)
async def update_task(
    task_uuid: str,
    request: TaskUpdateRequest,
    task_controller: TaskController = Depends(Factory().get_task_controller),
    current_user: int = Depends(get_current_user),
) -> TaskUpdateResponse:
    return await task_controller.update_task(
        uuid=task_uuid, owner_id=current_user.id, update_data=dict(request)
    )
