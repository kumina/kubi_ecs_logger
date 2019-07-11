from datetime import datetime

from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema


class Event(FieldSet):

    def __init__(self,
                 action: str = None,
                 category: str = None,
                 created: datetime = None,
                 dataset: str = None,
                 duration: int = None,
                 end: datetime = None,
                 hash: str = None,
                 id: str = None,
                 kind: str = None,
                 module: str = None,
                 original: str = None,
                 outcome: str = None,
                 risk_score: float = None,
                 risk_score_norm: float = None,
                 severity: int = None,
                 start: datetime = None,
                 timezone: str = None,
                 type: str = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.action = action
        self.category = category
        self.created = created
        self.dataset = dataset
        self.duration = duration
        self.end = end
        self.hash = hash
        self.id = id
        self.kind = kind
        self.module = module
        self.original = original
        self.outcome = outcome
        self.risk_score = risk_score
        self.risk_score_norm = risk_score_norm
        self.severity = severity
        self.start = start
        self.timezone = timezone
        self.type = type


class EventSchema(FieldSetSchema):
    action = fields.String()
    category = fields.String()
    created = fields.DateTime(format="iso")
    dataset = fields.String()
    duration = fields.Integer()
    end = fields.DateTime(format="iso")
    hash = fields.String()
    id = fields.String()
    kind = fields.String()
    module = fields.String()
    original = fields.String()
    outcome = fields.String()
    risk_score = fields.Float()
    risk_score_norm = fields.Float()
    severity = fields.Integer()
    start = fields.DateTime(format="iso")
    timezone = fields.String()
    type = fields.String()
