from flask import Blueprint
from flask_restful import Api
from .resources import *

auth_bp = Blueprint('auth', __name__)
api = Api(auth_bp)

api.add_resource(SignUpApi, '/api/auth/register/')
api.add_resource(LoginApi, '/api/auth/login/')
api.add_resource(ForgotPassword, '/api/auth/forgot-password/')
api.add_resource(ResetPassword, '/api/auth/reset-password/<token>/')