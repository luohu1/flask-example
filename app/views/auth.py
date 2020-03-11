# coding: utf-8
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from flask_restful import Api, Resource

app = Blueprint('auth', __name__, url_prefix='/auth')
api = Api(app)


class Login(Resource):
    def post(self):
        if not request.is_json:
            return jsonify({"msg": "Missing JSON in request"})

        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if not username or not password:
            return jsonify({"msg": "Missing username/password parameter"})

        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)


class Logout(Resource):
    def get(self):
        return "logout"


api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
