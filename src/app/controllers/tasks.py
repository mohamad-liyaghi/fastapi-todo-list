from core.controller import BaseController
from app.repositories import TaskRepository


class TaskController(BaseController):
    def __init__(self, task_repository: TaskRepository):
        self.model_class = None #TODO implement Task model
        self.repository = task_repository
