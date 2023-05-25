from typing import Type, TypeVar, List, Optional
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import select
from functools import reduce

from core.database import Base

ModelType = TypeVar('ModelType', bound=Base)


class BaseRepository:
    '''Base Data Repository'''

    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self.model_class = model
        self.session = session

    async def create(self, attributes: dict) -> ModelType:
        '''
        Create a new model instance.
        :param attributes: the data for creating object
        :return: The created object.
        '''

        model = self.model_class(**attributes)
        self.session.add(model)
        return model

    async def update(self, model: ModelType, update_data: dict) -> ModelType:
        """
        Updates the given model instance with the given data.

        :param model: The model instance to update.
        :param update_data: A dictionary containing the new data to update the model with.
        :return: The updated model instance.
        """

        for key, value in update_data.items():
            setattr(model, key, value)

        self.session.add(model)
        return model

    async def delete(self, model: ModelType) -> None:
        """
        Deletes the model instance.

        :param model: The model to delete.
        :return: None
        """
        self.session.delete(model)

    async def get_all(self, limit: int = 20, **kwargs) -> List[ModelType]:
        """
        Retrieves all model instances that match the specified criteria.

        :param limit: The maximum number of results to return.
        :param kwargs: Filter criteria.
        :return: A list of model instances, up to the specified limit.
        """
        query = await self._get_base_query(limit=limit, **kwargs)
        result = await self.session.execute(query)
        models = result.scalars().all()
        return models

    async def get_one(self, limit: int = None, **kwargs) -> Optional[ModelType]:
        """
        Retrieves the first model instance that matches the specified criteria.

        :param limit: The maximum number of results to return.
        :param kwargs: Filter criteria.
        :return: The model instance that matches the specified criteria, or None if not found.
        """
        query = await self._get_base_query(limit=limit, **kwargs)
        result = await self.session.execute(query)
        model = result.scalars().first()
        return model

    async def _get_base_query(self, limit: int = None, **kwargs):
        """
        Constructs a base query object based on the specified filter criteria and limit.

        :param limit: The maximum number of results to return.
        :param kwargs: Filter criteria.
        :return: A base query object.
        """
        query = select(self.model_class)
        filters = [getattr(self.model_class, field) == value for field, value in kwargs.items()]
        if filters:
            query = query.where(reduce(and_, filters))
        if limit is not None:
            query = query.limit(limit)
        return query
