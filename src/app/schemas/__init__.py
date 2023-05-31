from .requests.user import UserRegisterRequest
from .responses.user import UserRegisterResponse, UserAccessTokenResponse
from .requests.task import TaskCreateRequest, TaskUpdateRequest
from .responses.task import TaskCreateResponse, TaskUpdateResponse, TaskRetrieveResponse

USER_REQUEST = [
    'UserRegisterRequest',
]
USER_RESPONSE = [
    'UserRegisterResponse',
    'UserAccessTokenResponse',
]

TASK_REQUEST = [
    'TaskCreateRequest',
    'TaskUpdateRequest',
]
TASK_RESPONSE = [
    'TaskCreateResponse',
    'TaskUpdateResponse',
    'TaskRetrieveResponse',
]

__all__ = [
    *USER_REQUEST,
    *USER_RESPONSE,
    *TASK_REQUEST,
    *TASK_RESPONSE
]
