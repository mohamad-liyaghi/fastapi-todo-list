from core.controller import BaseController
from app.repositories import TaskRepository
from app.models import Task


class TaskController(BaseController):
    def __init__(self, task_repository: TaskRepository):
        self.model_class = Task
        self.repository = task_repository
