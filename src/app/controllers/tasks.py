from fastapi import HTTPException, status
from uuid import UUID
from core.controller import BaseController
from app.repositories import TaskRepository
from app.models import Task


class TaskController(BaseController):
    def __init__(self, task_repository: TaskRepository):
        self.model_class = Task
        self.repository = task_repository

    async def get_user_task_by_uuid(self, uuid: UUID, owner_id: int):
        task = await self.repository.get_one(uuid=uuid)

        if not task:
            raise HTTPException(
                detail='Task with given uuid didnt found',
                status_code=status.HTTP_404_NOT_FOUND
            )

        if task.owner_id != owner_id:
            raise HTTPException(
                detail='You can only update your own tasks.',
                status_code=status.HTTP_403_FORBIDDEN
            )
        return task

    async def update_task(self, uuid: UUID, owner_id: int, update_data):
        task = await self.get_user_task_by_uuid(uuid=uuid, owner_id=owner_id) 

        return await self.repository.update(
            model=task,
            **update_data
        )
