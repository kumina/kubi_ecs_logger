"""
TODO: Add doc what this file is doing
"""
from marshmallow import Schema, post_dump


class RootSchema(Schema):
    SKIP_VALUES = [None]

    @post_dump
    def remove_skip_values(self, data):
        return {
            key: value for key, value in data.items()
            if value not in self.SKIP_VALUES
        }

    @post_dump(pass_original=True)
    def add_extra(self, serialized, original):
        from kubi_ecs_logger.models.include import INCLUDE_FIELDS

        for k, v in original.__dict__.items():
            if k not in serialized and v is not None:
                type_name = str(type(v).__name__).lower()
                if type_name in INCLUDE_FIELDS:
                    schema = INCLUDE_FIELDS[type_name].schema
                    data = schema.dump(v).data
                    if "kind" not in data:
                        data["kind"] = type_name
                    serialized[k] = data
                elif isinstance(v, (int, float, str, bool, dict)):
                    if not str(k).startswith('_'):
                        serialized[k] = v

        return serialized
