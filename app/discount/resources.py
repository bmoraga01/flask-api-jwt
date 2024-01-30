from flask import request
from flask_restful import Resource

from .schemas import *
from .models import *

from ..common.error_handling import ObjectNotFound

discountType_schema = DiscountTypeSchema()
discount_schema = DiscountSchema()

class DiscountTypeListResource(Resource):
    def get(self):
        discountType = DiscountType.get_all()
        result = discountType_schema.dump(discountType, many=True)
        return result
    
    def post(self):
        data = request.get_json()
        discountType_dict = discountType_schema.load(data)
        
        discountType = DiscountType(msdt_id=discountType_dict['msdt_id'], msdt_desc=discountType_dict['msdt_desc'], msdt_active_status=discountType_dict['msdt_active_status'])
        discountType.save()
        
        resp = discountType_schema.dump(discountType)
        return resp, 201
        
class DiscountListResource(Resource):
    def get(self):
        discount = Discount.get_all()
        result = discount_schema.dump(discount, many=True)
        return result
    
    def post(self):
        data = request.get_json()
        discount_dict = discount_schema.load(data)
        
        discount = Discount(msd_id=discount_dict['msd_id'], msd_msdt_id=discount_dict['msd_msdt_id'], msd_desc=discount_dict['msd_desc'], msd_nominal=discount_dict['msd_nominal'], msd_active_status=discount_dict['msd_active_status'])
        discount.save()
        
        result = discount_schema.dump(discount)
        
        return result, 201
    
class DiscountResource(Resource):
    def get(self, id):
        discount = Discount.get_by_id(id)
        
        if discount is None:
            raise ObjectNotFound('El descuento no existe')
        
        resp = discount_schema.dump(discount)
        return resp