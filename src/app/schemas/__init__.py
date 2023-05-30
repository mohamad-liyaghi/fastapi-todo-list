from .requests.user import UserRegisterRequest
from .responses.user import UserRegisterResponse, UserAccessTokenResponse
from .requests.task import TaskCreateRequest
from .responses.task import TaskCreateResponse

USER_REQUEST = [
    'UserRegisterRequest',
]
USER_RESPONSE = [
    'UserRegisterResponse',
    'UserAccessTokenResponse',
]

TASK_REQUEST = [
    'TaskCreateRequest',
]
TASK_RESPONSE = [
    'TaskCreateResponse',
]

__all__ = [
    *USER_REQUEST,
    *USER_RESPONSE,
    *TASK_REQUEST,
    *TASK_RESPONSE
]
