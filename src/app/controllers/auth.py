from core.controller import BaseController
from app.repositories import UserRepository


class AuthController(BaseController):
    def __init__(self, user_repository: UserRepository):
        # TODO add model
        self.model_class = None
        self.repository = user_repository
