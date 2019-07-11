from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema


class Agent(FieldSet):

    def __init__(self,
                 ephemeral_id: str = None,
                 id: str = None,
                 name: str = None,
                 type: str = None,
                 version: str = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ephemeral_id = ephemeral_id
        self.id = id
        self.name = name
        self.type = type
        self.version = version


class AgentSchema(FieldSetSchema):
    ephemeral_id = fields.String()
    id = fields.String()
    name = fields.String()
    type = fields.String()
    version = fields.String()
