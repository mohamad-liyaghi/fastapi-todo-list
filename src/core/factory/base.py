from fastapi import Depends

from app.controllers import AuthController, UserController, TaskController
from app.repositories import UserRepository, TaskRepository
from app.models import User, Task
from core.database import get_session


class Factory:
    """
    This is the factory container that will instantiate all the controllers and
    repositories which can be accessed by the rest of the application.
    """

    # Repositories
    user_repository = UserRepository
    task_repository = TaskRepository

    def get_user_controller(self, session=Depends(get_session)):
        return UserController(
            user_repository=self.user_repository(session=session, model=User)
        )

    def get_auth_controller(self, session=Depends(get_session)):
        return AuthController(
            user_repository=self.user_repository(session=session, model=User),
        )

    def get_task_controller(self, session=Depends(get_session)):
        return TaskController(
            task_repository=self.task_repository(session=session, model=Task),
        )
