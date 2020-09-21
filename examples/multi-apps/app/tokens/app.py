from flask import Blueprint
from flask_restful import Api

from .views import Token

app = Blueprint('tokens', __name__, url_prefix='/tokens')
api = Api(app)

api.add_resource(Token, '/')
