from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema


class Observer(FieldSet):

    def __init__(self,
                 hostname: str = None,
                 ip: str = None,
                 mac: str = None,
                 serial_number: str = None,
                 type: str = None,
                 vendor: str = None,
                 version: str = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.hostname = hostname
        self.ip = ip
        self.mac = mac
        self.serial_number = serial_number
        self.type = type
        self.vendor = vendor
        self.version = version


class ObserverSchema(FieldSetSchema):
    hostname = fields.String()
    ip = fields.String()
    mac = fields.String()
    serial_number = fields.String()
    type = fields.String()
    vendor = fields.String()
    version = fields.String()
