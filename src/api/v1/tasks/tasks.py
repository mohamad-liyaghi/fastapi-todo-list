from fastapi import Depends, status
from fastapi.routing import APIRouter
from core.dependencies import AuthenticationRequired
from app.controllers import TaskController
from core.factory import Factory
from app.schemas import TaskCreateRequest, TaskCreateResponse
from core.dependencies import get_current_user

router = APIRouter()


@router.post(
        '/create',
        dependencies=[Depends(AuthenticationRequired)],
        status_code=status.HTTP_201_CREATED,
)
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
