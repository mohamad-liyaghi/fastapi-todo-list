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
    TaskRetrieveResponse,
    TaskListResponse,
)
from core.dependencies import get_current_user
from uuid import UUID
from typing import List


router = APIRouter(
    dependencies=[Depends(AuthenticationRequired)],
)


@router.get('/', status_code=status.HTTP_200_OK)
async def retrieve_all_tasks(
    task_controller: TaskController = Depends(Factory().get_task_controller),
    current_user: int = Depends(get_current_user),
) -> List[TaskListResponse]:

    tasks = await task_controller.get_user_task_list(owner_id=current_user.id)
    return tasks


@router.get('/detail/{task_uuid}/', status_code=status.HTTP_200_OK)
async def retrieve_task(
    task_uuid: UUID,
    task_controller: TaskController = Depends(Factory().get_task_controller),
    current_user: int = Depends(get_current_user),
) -> TaskRetrieveResponse:

    return await task_controller.get_user_task_by_uuid(
        uuid=task_uuid, owner_id=current_user.id
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
    task_uuid: UUID,
    request: TaskUpdateRequest,
    task_controller: TaskController = Depends(Factory().get_task_controller),
    current_user: int = Depends(get_current_user),
) -> TaskUpdateResponse:
    return await task_controller.update_task(
        uuid=task_uuid, owner_id=current_user.id, update_data=dict(request)
    )


@router.delete('/delete/{task_uuid}/', status_code=status.HTTP_200_OK)
async def delete_task(
    task_uuid: UUID,
    task_controller: TaskController = Depends(Factory().get_task_controller),
    current_user: int = Depends(get_current_user),
):

    await task_controller.delete_task(
        uuid=task_uuid, owner_id=current_user.id
    )
    return {'success': 'deleted'}
