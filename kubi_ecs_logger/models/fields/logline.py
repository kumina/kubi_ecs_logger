from typing import Union
from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema
from ..severity import Severity


class LogLine(FieldSet):

    def __init__(self,
                 level: Union[str, Severity] = None,
                 original: str = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)

        if isinstance(level, Severity):
            level = level.name

        self.__level = level
        self.original = original

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        assert isinstance(value, Severity)
        self.__level = value.name


class LogLineSchema(FieldSetSchema):
    level = fields.String()
    original = fields.String()
