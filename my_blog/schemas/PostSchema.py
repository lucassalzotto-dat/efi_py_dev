
from marshmallow import Schema, fields, validate

class PostSchema(Schema):
    id = fields.Integer(dump_only=True)
    author = fields.Integer(required=True)
    title = fields.String(required=True, validate=validate.Length(max=100))
    body = fields.String(required=True)
    dateTime = fields.DateTime(dump_only=True)
