from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema


class Network(FieldSet):

    def __init__(self,
                 application: str = None,
                 bytes: int = None,
                 community_id: str = None,
                 direction: str = None,
                 forwarded_ip: str = None,
                 iana_number: str = None,
                 name: str = None,
                 packets: int = None,
                 protocol: str = None,
                 transport: str = None,
                 type: str = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.application = application
        self.bytes = bytes
        self.community_id = community_id
        self.direction = direction
        self.forwarded_ip = forwarded_ip
        self.iana_number = iana_number
        self.name = name
        self.packets = packets
        self.protocol = protocol
        self.transport = transport
        self.type = type


class NetworkSchema(FieldSetSchema):
    application = fields.String()
    bytes = fields.Integer()
    community_id = fields.String()
    direction = fields.String()
    forwarded_ip = fields.String()
    iana_number = fields.String()
    name = fields.String()
    packets = fields.Integer()
    protocol = fields.String()
    transport = fields.String()
    type = fields.String()
