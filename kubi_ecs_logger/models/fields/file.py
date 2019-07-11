from datetime import datetime
from marshmallow import fields

from .field_set import FieldSet, FieldSetSchema


class File(FieldSet):

    def __init__(self,
                 ctime: datetime = None,
                 device: str = None,
                 extension: str = None,
                 gid: str = None,
                 group: str = None,
                 inode: str = None,
                 mode: str = None,
                 mtime: datetime = None,
                 owner: str = None,
                 path: str = None,
                 size: int = None,
                 target_path: str = None,
                 type: str = None,
                 uid: str = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctime = ctime
        self.device = device
        self.extension = extension
        self.gid = gid
        self.group = group
        self.inode = inode
        self.mode = mode
        self.mtime = mtime
        self.owner = owner
        self.path = path
        self.size = size
        self.target_path = target_path
        self.type = type
        self.uid = uid


class FileSchema(FieldSetSchema):
    ctime = fields.DateTime(format="iso")
    device = fields.String()
    extension = fields.String()
    gid = fields.String()
    group = fields.String()
    inode = fields.String()
    mode = fields.String()
    mtime = fields.DateTime(format="iso")
    owner = fields.String()
    path = fields.String()
    size = fields.Integer()
    target_path = fields.String()
    type = fields.String()
    uid = fields.String()

