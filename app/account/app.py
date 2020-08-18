from flask import Blueprint
from flask_restful import Api

from .views import UserDetail, UserList

app = Blueprint('users', __name__, url_prefix='/users')
api = Api(app)

api.add_resource(UserList, '/')
api.add_resource(UserDetail, '/<name>')
