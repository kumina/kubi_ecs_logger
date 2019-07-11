from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema


class Cloud(FieldSet):

    def __init__(self,
                 account_id: str = None,
                 availability_zone: str = None,
                 instance_id: str = None,
                 instance_name: str = None,
                 machine_type: str = None,
                 provider: str = None,
                 region: str = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.account_id = account_id
        self.availability_zone = availability_zone
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.machine_type = machine_type
        self.provider = provider
        self.region = region


class CloudSchema(FieldSetSchema):
    account_id = fields.String()
    availability_zone = fields.String()
    instance_id = fields.String()
    instance_name = fields.String()
    machine_type = fields.String()
    provider = fields.String()
    region = fields.String()
