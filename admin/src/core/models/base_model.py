"""Base model for the database."""
from src.core.database import db
from src.core.models.site_config import SiteConfig
from datetime import datetime


class BaseModel(db.Model):
    """Base Model."""

    __abstract__ = True

    @classmethod
    def update(cls, entity_id, **kwargs):
        """
        Update an existing object of a model with the given ID.

        Args:
            id (int): The ID of the entity to be updated.
            **kwargs: Keyword arguments representing the attributes to update.

        Returns:
            Entity: The updated entity object.
        """
        entity = cls.query.get(entity_id)
        if entity:
            for key, value in kwargs.items():
                setattr(entity, key, value)
            entity.updated_at = datetime.utcnow()
            db.session.commit()
            return entity
        else:
            return None

    @classmethod
    def delete(cls, entity_id: int):
        """
        Delete an object of an model with the given ID.

        Args:
            entity_id (int): The ID of the entity to be deleted.

        Returns:
            int: The number of rows deleted.
        """
        entity_id = cls.query.filter_by(id=entity_id).delete()
        db.session.commit()
        return entity_id

    @classmethod
    def get_by_id(cls, id: int):
        """
        Get an object of a model with the given ID.

        Args:
            id (int): The ID of the entity to be retrieved.

        Returns:
            Entity: The entity object.
        """
        return cls.query.filter_by(id=id).first()

    @classmethod
    def get_all(cls):
        """
        Get all objects of the given class in the database.

        Returns:
            List[Entity]: A list of entity objects.
        """
        return cls.query.all()

    @classmethod
    def get_paginated(cls, page: int, per_page: int = None):
        """
        Get all objects of the given class in the database paginated.

        If no per_page is specified, the default value is
        SiteConfig.get_items_per_page().

        Args:
            page (int): The page number to be retrieved.
            per_page (int, optional): The number of items per page.
            Defaults to None.

        Returns:
            SQLAlchemy.orm.PaginatedResult: The paginated result object.
        """
        if per_page is None:
            per_page = SiteConfig.get_items_per_page()
        return cls.query.paginate(
            page=page, per_page=per_page, error_out=False
        )

    @classmethod
    def get_query_paginated(cls, query, page, per_page=None):
        """
        Get a previous query paginated.

        If no per_page is specified, the default value is
        SiteConfig.get_items_per_page().

        Args:
            query (SQLAlchemy.orm.Query): The query to be paginated.
            page (int): The page number to be retrieved.
            per_page (int, optional): The number of items per page.
            Defaults to None.

        Returns:
            SQLAlchemy.orm.PaginatedResult: The paginated result object.
        """
        if per_page is None:
            per_page = SiteConfig.get_items_per_page()
        return query.paginate(page=page, per_page=per_page, error_out=False)

    @classmethod
    def get_by(cls, field, data):
        """Return an object of a model with the given field and value."""
        return cls.query.filter_by(**{field: data}).first()
