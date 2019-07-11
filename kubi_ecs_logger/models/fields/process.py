from datetime import datetime
from typing import List

from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema


class Process(FieldSet):

    def __init__(self,
                 args: List[str] = None,
                 executable: str = None,
                 name: str = None,
                 pid: int = None,
                 ppid: int = None,
                 start: datetime = None,
                 thread_id: int = None,
                 title: str = None,
                 working_directory: str = None,
                 *aargs, **kwargs):
        super().__init__(*aargs, **kwargs)
        self.args = args
        self.executable = executable
        self.name = name
        self.pid = pid
        self.ppid = ppid
        self.start = start
        self.thread_id = thread_id
        self.title = title
        self.working_directory = working_directory


class ProcessSchema(FieldSetSchema):
    args = fields.List(fields.String())
    executable = fields.String()
    name = fields.String()
    pid = fields.Integer()
    ppid = fields.Integer()
    start = fields.DateTime(format="iso")
    thread_id = fields.Integer()
    title = fields.String()
    working_directory = fields.String()
