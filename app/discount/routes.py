from flask import Blueprint
from flask_restful import Api
from .resources import *

discount_bp = Blueprint('discount', __name__)

api = Api(discount_bp)

api.add_resource(DiscountTypeListResource, '/api/discount-type', endpoint='discount_type_list')

api.add_resource(DiscountListResource, '/api/discount', endpoint='discount_list')
api.add_resource(DiscountResource, '/api/discount/<int:pk>', endpoint='discount_detail')