from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema


class OS(FieldSet):

    def __init__(self,
                 family: str = None,
                 full: str = None,
                 kernel: str = None,
                 name: str = None,
                 platform: str = None,
                 version: str = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.family = family
        self.full = full
        self.kernel = kernel
        self.name = name
        self.platform = platform
        self.version = version


class OSSchema(FieldSetSchema):
    family = fields.String()
    full = fields.String()
    kernel = fields.String()
    name = fields.String()
    platform = fields.String()
    version = fields.String()
