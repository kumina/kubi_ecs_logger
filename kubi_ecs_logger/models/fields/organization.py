from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema


class Organization(FieldSet):

    def __init__(self,
                 id: str = None,
                 name: str = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id
        self.name = name


class OrganizationSchema(FieldSetSchema):
    id = fields.String()
    name = fields.String()
