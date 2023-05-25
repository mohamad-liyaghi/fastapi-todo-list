from typing import Any, Generic, Type, TypeVar, List
from uuid import UUID

from core.database import Base
from core.repository import BaseRepository
from core.exceptions import NotFoundException

ModelType = TypeVar('ModelType', bound=Base)


class BaseController(Generic[ModelType]):
    """Base class for data controllers."""
    def __init__(self, model: Type[ModelType], repository: BaseRepository):
        self.model_class = model
        self.repository = repository

    async def get_by_id(self, id_: int) -> ModelType:
        """
        Returns the model instance matching the id.

        :param id_: The id to match.
        :return: The model instance.
        """
        obj = await self.repository.get_one(id=id_)
        if not obj:
            raise NotFoundException(f"{self.model_class.__tablename__.title()} with id: {id_} does not exist")
        return obj

    async def get_by_uuid(self, uuid: UUID) -> ModelType:
        """
        Returns the model instance matching the uuid.

        :param uuid: The uuid to match.
        :return: The model instance.
        """
        obj = await self.repository.get_one(uuid=uuid)
        if not obj:
            raise NotFoundException(f"{self.model_class.__tablename__.title()} with uuid: {uuid} does not exist")
        return obj    
    
    async def get_all(self, limit: int = 20) -> List[ModelType]:
        """
        Returns a list of all model instances.

        :return: A list of all model instances.
        """
        return await self.repository.get_all(limit=limit)

    async def create(self, **attributes) -> ModelType:
        """
        Creates a new model instance with the given attributes.

        :param attributes: A dictionary containing the attributes of the new model instance.
        :return: The created model instance.
        """
        return await self.repository.create(**attributes)

    async def delete(self, id_: int) -> None:
        """
        Deletes the model instance with the given id.

        :param id_: The id of the model instance to delete.
        :return: None
        """
        obj = await self.repository.get_one(id_=id_)
        if not obj:
            raise NotFoundException(
                f"{self.model_class.__tablename__.title()} with id: {id_} does not exist"
            )
        await self.repository.delete(obj)
