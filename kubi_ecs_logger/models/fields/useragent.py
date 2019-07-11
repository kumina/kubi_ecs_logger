from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema


class UserAgent(FieldSet):

    def __init__(self,
                 device_name: str = None,
                 name: str = None,
                 original: str = None,
                 version: str = None,
                 *aargs, **kwargs):
        super().__init__(*aargs, **kwargs)
        self.device_name = device_name
        self.name = name
        self.original = original
        self.version = version

class UserAgentSchema(FieldSetSchema):
    device_name = fields.String()
    name = fields.String()
    original = fields.String()
    version = fields.String()


