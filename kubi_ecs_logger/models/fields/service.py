from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema


class Service(FieldSet):

    def __init__(self,
                 ephemeral_id: str = None,
                 id: str = None,
                 name: str = None,
                 state: str = None,
                 type: str = None,
                 version: str = None,
                 *aargs, **kwargs):
        super().__init__(*aargs, **kwargs)
        self.ephemeral_id = ephemeral_id
        self.id = id
        self.name = name
        self.state = state
        self.type = type
        self.version = version


class ServiceSchema(FieldSetSchema):
    ephemeral_id = fields.String()
    id = fields.String()
    name = fields.String()
    state = fields.String()
    type = fields.String()
    version = fields.String()
