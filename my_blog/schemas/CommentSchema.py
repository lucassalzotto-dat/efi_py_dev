
from marshmallow import Schema, fields

class CommentSchema(Schema):
    id = fields.Integer(dump_only=True)
    texto = fields.String(required=True)
    fecha_creacion = fields.DateTime(dump_only=True)
    autor_id = fields.Integer(required=True)
    post_id = fields.Integer(required=True)
