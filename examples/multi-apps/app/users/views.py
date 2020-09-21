from flask import jsonify, request
from flask_jwt_extended import create_access_token
from flask_restful import Resource

from .models import UserModel


class UserList(Resource):
    def get(self):
        users = UserModel.query.all()
        data = []
        for u in users:
            data.append(u.to_dict())
        return jsonify(data=data)

    def post(self):
        raw_data = request.get_json()
        user = UserModel(**raw_data)
        user.save()
        return jsonify(msg=str(user))


class UserDetail(Resource):
    def get(self, name):
        user = UserModel.query.filter_by(username=name).first_or_404()
        return jsonify(data=user.to_dict())


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
