# coding: utf-8
from flask import Blueprint
from flask_restful import Api, Resource

app = Blueprint('auth', __name__)
api = Api(app)


class Login(Resource):
    def post(self):
        return "login"


class Logout(Resource):
    def get(self):
        return "logout"


api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
