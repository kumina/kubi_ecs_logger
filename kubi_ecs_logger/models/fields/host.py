from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema


class Host(FieldSet):

    def __init__(self,
                 architecture: str = None,
                 hostname: str = None,
                 id: str = None,
                 ip: str = None,
                 mac: str = None,
                 name: str = None,
                 type: str = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.architecture = architecture
        self.hostname = hostname
        self.id = id
        self.ip = ip
        self.mac = mac
        self.name = name
        self.type = type


class HostSchema(FieldSetSchema):
    architecture = fields.String()
    hostname = fields.String()
    id = fields.String()
    ip = fields.String()
    mac = fields.String()
    name = fields.String()
    type = fields.String()
