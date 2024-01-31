from marshmallow import fields, ValidationError
from app.ext import ma

def read_only(val):
    if val is not fields.missing:
        raise ValidationError('Cannot pass a read-only field.')

class DiscountSchema(ma.Schema):
    id = fields.Int(data_key='discount_id', validate=read_only)
    dt_id = fields.Int(data_key='dt_id')
    desc = fields.Str(data_key='desc')
    nominal = fields.Int(data_key='discount_nominal')
    active_status = fields.Str(data_key='active_status')
    discount_type = fields.Nested('DiscountTypeSchema', only=('id', 'desc','active_status'))

class DiscountTypeSchema(ma.Schema):
    """
        Schema to retrieve data from Model Discount Type as dictionary.
        data_key is an alias for column name.
    """
    
    id = fields.Int(data_key='discount_type_id', validate=read_only)
    desc = fields.Str(data_key='discount_type')
    active_status = fields.Str(data_key='active_status')