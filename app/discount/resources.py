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
        
        discountType = DiscountType(desc=discountType_dict['desc'], active_status=discountType_dict['active_status'])
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
        print(data)
        discount_dict = discount_schema.load(data)
        
        discount = Discount(dt_id=discount_dict['dt_id'], desc=discount_dict['desc'], nominal=discount_dict['nominal'], active_status=discount_dict['active_status'])
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