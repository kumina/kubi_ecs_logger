from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema


class User(FieldSet):

    def __init__(self,
                 email: str = None,
                 full_name: str = None,
                 hash: str = None,
                 id: str = None,
                 name: str = None,
                 *aargs, **kwargs):
        super().__init__(*aargs, **kwargs)
        self.email = email
        self.full_name = full_name
        self.hash = hash
        self.id = id
        self.name = name


class UserSchema(FieldSetSchema):
    email = fields.String()
    full_name = fields.String()
    hash = fields.String()
    id = fields.String()
    name = fields.String()

