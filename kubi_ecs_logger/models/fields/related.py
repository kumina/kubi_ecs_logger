from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema


class Related(FieldSet):

    def __init__(self,
                 ip: str = None,
                 *aargs, **kwargs):
        super().__init__(*aargs, **kwargs)
        self.ip = ip


class RelatedSchema(FieldSetSchema):
    ip = fields.String()

