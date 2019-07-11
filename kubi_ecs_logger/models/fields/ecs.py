from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema


class ECS(FieldSet):

    def __init__(self,
                 version: str = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.version = version


class ECSSchema(FieldSetSchema):
    version = fields.String()
