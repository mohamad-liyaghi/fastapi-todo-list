from fastapi import Depends

from app.controllers import AuthController, UserController
from app.repositories import UserRepository
from app.models import User
from core.database import get_session


class Factory:
    """
    This is the factory container that will instantiate all the controllers and
    repositories which can be accessed by the rest of the application.
    """

    # Repositories
    user_repository = UserRepository

    def get_user_controller(self, db_session=Depends(get_session)):
        return UserController(
            user_repository=self.user_repository(db_session=db_session)
        )

    def get_auth_controller(self, session=Depends(get_session)):
        return AuthController(
            user_repository=self.user_repository(session=session, model=User),
        )
