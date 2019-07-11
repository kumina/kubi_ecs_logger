from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema


class Error(FieldSet):

    def __init__(self,
                 code: str = None,
                 id: str = None,
                 message: str = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.code = code
        self.id = id
        self.message = message


class ErrorSchema(FieldSetSchema):
    code = fields.String()
    id = fields.String()
    message = fields.String()
