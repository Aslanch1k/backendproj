from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)


class CategorySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)

class RecordQuerySchema(Schema):
    user_id = fields.Int(required=True)
    category_id = fields.Str()


class RecordSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    category_id = fields.Int(required=True)
    sum = fields.Float(required=True)

class CurrencySchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    currency_to_usd = fields.Float(required=False)
