from marshmallow import fields
from app.ext import ma

class DiscountSchema(ma.Schema):
    msd_id = fields.Int(data_key='discount_id')
    msd_msdt_id = fields.Int(data_key='dt_id')
    msd_desc = fields.Str(data_key='desc')
    msd_nominal = fields.Int(data_key='discount_nominal')
    msd_active_status = fields.Str(data_key='active_status')
    discount_type = fields.Nested('DiscountTypeSchema', only=('msdt_id', 'msdt_desc','msdt_active_status'))

class DiscountTypeSchema(ma.Schema):
    """
        Schema to retrieve data from Model Discount Type as dictionary.
        data_key is an alias for column name.
    """
    
    msdt_id = fields.Int(data_key='discount_type_id')
    msdt_desc = fields.Str(data_key='discount_type')
    msdt_active_status = fields.Str(data_key='active_status')