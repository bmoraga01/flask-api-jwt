from flask import Response, request, make_response
from flask_restful import Resource
from .service import *

from .schemas import *
from .models import *

from ..common.error_handling import ObjectNotFound

class SignUpApi(Resource):
    @staticmethod
    def post() -> Response:
        """
        
        POST response method for creating user.
        :return: JSON object
        
        """
        input_data = request.get_json()
        response, status = create_user(request, input_data)
        return make_response(response, status)
    
class LoginApi(Resource):
    @staticmethod
    def post() -> Response:
        """
        
        POST response method for login user.
        :return: JSON object
        
        """
        input_data = request.get_json()
        response, status = login_user(request, input_data)
        return make_response(response, status)
    
class ForgotPassword(Resource):
    @staticmethod
    def post() -> Response:
        """
        
        POST response method for forgot password email send user.
        :return: JSON object
        
        """
        input_data = request.get_json()
        response, status = reset_password_email_send(request, input_data)
        return make_response(response, status)
    
class ResetPassword(Resource):
    @staticmethod
    def post(token) -> Response:
        """
        
        POST response method for save new password.
        :return: JSON object
        
        """
        input_data = request.get_json()
        response, status = reset_password(request, input_data, token)
        return make_response(response, status)