# coding: utf-8
from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token
from flask_restful import Api, Resource

from app.models.user import UserModel

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

        user = UserModel.query.filter_by(username=username).first_or_404()
        if user:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)

        return jsonify({"msg": "User not found"})


class Logout(Resource):
    def get(self):
        return "logout"


api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
