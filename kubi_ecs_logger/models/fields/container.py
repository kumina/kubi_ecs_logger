from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema


class Container(FieldSet):

    def __init__(self,
                 id: str = None,
                 image_name: str = None,
                 image_tag: str = None,
                 labels: dict = None,
                 name: str = None,
                 runtime: str = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.id = id
        self.image_name = image_name
        self.image_tag = image_tag
        self.labels = labels
        self.name = name
        self.runtime = runtime


class ContainerSchema(FieldSetSchema):
    id = fields.String()
    image_name = fields.String()
    image_tag = fields.String()
    labels = fields.Dict()
    name = fields.String()
    runtime = fields.String()
