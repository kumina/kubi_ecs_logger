from marshmallow import post_load
from kubi_ecs_logger.models import RootSchema


class FieldSet:

    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            if not hasattr(self, k):
                setattr(self, k, v)


class FieldSetSchema(RootSchema):
    class Meta:
        model = FieldSet

    @post_load
    def load_data(self, data):
        return FieldSet(**data)


