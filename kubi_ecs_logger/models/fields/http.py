from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema


class HttpRequest(FieldSet):

    def __init__(self,
                 body_bytes: int = None,
                 body_content: str = None,
                 bytes: int = None,
                 method: str = None,
                 referrer: str = None,
                 version: str = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.body_bytes = body_bytes
        self.body_content = body_content
        self.bytes = bytes
        self.method = method
        self.referrer = referrer
        self.version = version


class HttpRequestSchema(FieldSetSchema):
    body_bytes = fields.Integer()
    body_content = fields.String()
    bytes = fields.Integer()
    method = fields.String()
    referrer = fields.String()
    version = fields.String()


class HttpResponse(FieldSet):

    def __init__(self,
                 body_bytes: int = None,
                 body_content: str = None,
                 bytes: int = None,
                 status_code: str = None,
                 version: str = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.body_bytes = body_bytes
        self.body_content = body_content
        self.bytes = bytes
        self.status_code = status_code
        self.version = version


class HttpResponseSchema(FieldSetSchema):
    body_bytes = fields.Integer()
    body_content = fields.String()
    bytes = fields.Integer()
    status_code = fields.String()
    version = fields.String()
