from flask import Blueprint
from flask_restful import Api

from .views import Login, Logout, UserDetail, UserList

app = Blueprint('users', __name__, url_prefix='/users')
api = Api(app)

api.add_resource(UserList, '/')
api.add_resource(UserDetail, '/<name>')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
