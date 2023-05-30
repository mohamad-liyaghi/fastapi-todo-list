from fastapi import Depends, status
from fastapi.routing import APIRouter
from core.dependencies import AuthenticationRequired
from app.controllers import TaskController
from core.factory import Factory
from app.schemas import TaskCreateRequest, TaskCreateResponse

router = APIRouter()


@router.post(
        '/create',
        dependencies=[Depends(AuthenticationRequired)],
        status_code=status.HTTP_201_CREATED
)
async def create_task(
    request: TaskCreateRequest,
    task_controller: TaskController = Depends(Factory().get_task_controller),
) -> TaskCreateResponse:
    # TODO add get user id
    task = await task_controller.create(
        title=request.title,
        description=request.description,
        owner_id=1
    )
    return task
