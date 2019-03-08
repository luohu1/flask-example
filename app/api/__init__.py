from flask import Blueprint
from flask_restful import Api

from .users import UserAPi

app = Blueprint('api', __name__)
api = Api(app)

api.add_resource(UserAPi, '/users')
