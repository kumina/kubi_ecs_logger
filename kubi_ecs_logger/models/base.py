from typing import List
from datetime import datetime

from marshmallow import fields

from kubi_ecs_logger.models import RootSchema
from kubi_ecs_logger.models.fields import FieldSet


class Base:

    def __init__(self,
                 date: datetime = None,
                 labels: dict = None,
                 message: str = None,
                 tags: List[str] = None,
                 objects: List[FieldSet] = None,
                 **kwargs):
        self.timestamp = date or datetime.now()
        self.labels = labels
        self.message = message
        self.tags = tags

        # Add custom fields from **kwargs
        for k, v in kwargs.items():
            if not hasattr(self, k):
                setattr(self, k, v)

        # Add the field objects that are passed
        if objects is not None:
            for obj in objects:
                if not self.add_object(obj):
                    raise ValueError(f"You can have only one of: {type(obj).__name__}")

    # Add a field object after initialization
    def add_object(self, obj) -> bool:
        assert isinstance(obj, FieldSet)
        name = str(type(obj).__name__).lower()
        if not hasattr(self, name):
            setattr(self, name, obj)
            return True
        return False


class BaseSchema(RootSchema):
    class Meta:
        include = {
            "@timestamp": fields.DateTime(format="iso", attribute="timestamp", allow_none=False)
        }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        from .include import INCLUDE_FIELDS
        self.declared_fields.update(INCLUDE_FIELDS)

    labels = fields.Dict(allow_none=False, skip_if=None)
    message = fields.String(allow_none=True)
    tags = fields.List(fields.String(), allow_none=True)
