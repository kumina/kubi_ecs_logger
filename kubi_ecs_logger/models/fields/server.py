from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema


class Server(FieldSet):

    def __init__(self,
                 address: str = None,
                 bytes: int = None,
                 domain: str = None,
                 ip: str = None,
                 mac: str = None,
                 packets: int = None,
                 port: int = None,
                 *aargs, **kwargs):
        super().__init__(*aargs, **kwargs)
        self.address = address
        self.bytes = bytes
        self.domain = domain
        self.ip = ip
        self.mac = mac
        self.packets = packets
        self.port = port


class ServerSchema(FieldSetSchema):
    address = fields.String()
    bytes = fields.Integer()
    domain = fields.String()
    ip = fields.String()
    mac = fields.String()
    packets = fields.Integer()
    port = fields.Integer()

