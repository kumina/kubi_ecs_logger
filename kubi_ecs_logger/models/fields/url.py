from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema


class Url(FieldSet):

    def __init__(self,
                 domain: str = None,
                 fragment: str = None,
                 full: str = None,
                 original: str = None,
                 password: str = None,
                 path: str = None,
                 port: int = None,
                 query: str = None,
                 scheme: str = None,
                 username: str = None,
                 *aargs, **kwargs):
        super().__init__(*aargs, **kwargs)
        self.domain = domain
        self.fragment = fragment
        self.full = full
        self.original = original
        self.password = password
        self.path = path
        self.port = port
        self.query = query
        self.scheme = scheme
        self.username = username


class UrlSchema(FieldSetSchema):
    domain = fields.String()
    fragment = fields.String()
    full = fields.String()
    original = fields.String()
    password = fields.String()
    path = fields.String()
    port = fields.Integer()
    query = fields.String()
    scheme = fields.String()
    username = fields.String()
