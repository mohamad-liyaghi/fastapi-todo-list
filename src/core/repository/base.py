from typing import Type, TypeVar, List, Optional
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import Base

ModelType = TypeVar('ModelType', bound=Base)


class BaseRepository:
    '''Base Data Repository'''

    def __init__(self, model: Type[ModelType], session: AsyncSession):
        self.model_class = model
        self.session = session

    async def create(self, **attributes) -> ModelType:
        '''
        Create a new model instance.
        :param attributes: the data for creating object
        :return: The created object.
        '''

        model = self.model_class(**attributes)
        self.session.add(model)
        await self.session.commit()
        return model

    async def update(self, model: ModelType, **update_data) -> ModelType:
        """
        Updates the given model instance with the given data.

        :param model: The model instance to update.
        :param update_data: A dictionary containing the new data to update
        the model with.
        :return: The updated model instance.
        """

        for key, value in update_data.items():
            setattr(model, key, value)

        self.session.add(model)
        await self.session.commit()
        return model

    async def delete(self, model: ModelType) -> None:
        """
        Deletes the model instance.

        :param model: The model to delete.
        :return: None
        """
        await self.session.delete(model)
        await self.session.commit()

    async def get_all(self, limit: int = 20, **kwargs) -> List[ModelType]:
        """
        Retrieves all model instances that match the specified criteria.

        :param limit: The maximum number of results to return.
        :param kwargs: Filter criteria.
        :return: A list of model instances, up to the specified limit.
        """
        query = await self._get_base_query(limit=limit, **kwargs)
        result = await self.session.execute(query)
        return result.all()

    async def get_one(self, **kwargs) -> Optional[ModelType]:
        """
        Retrieves the first model instance that matches the specified criteria.

        :param limit: The maximum number of results to return.
        :param kwargs: Filter criteria.
        :return: The model instance that matches the specified criteria,
        or None if not found.
        """
        query = await self._get_base_query(limit=1, **kwargs)
        result = await self.session.execute(query)
        model_id = result.scalars().first()
        if not model_id:
            return

        model = await self.session.get(self.model_class, model_id)
        return model

    async def _get_base_query(self, limit: int = None, **kwargs):
        """
        Constructs a base query object based on the specified filter criteria
        and limit.

        :param limit: The maximum number of results to return.
        :param kwargs: Filter criteria.
        :return: A base query object.
        """
        table = self.model_class.__table__
        query = select(table)
        filters = [
            table.columns[field] == value for field, value in kwargs.items()
        ]
        if filters:
            query = query.where(and_(*filters))
        if limit is not None:
            query = query.limit(limit)
        return query
