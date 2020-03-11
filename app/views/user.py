from flask import Blueprint, jsonify, request
from flask_restful import Api, Resource

from app.models.user import UserModel

app = Blueprint('users', __name__, url_prefix='/users')
api = Api(app)


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


api.add_resource(UserList, '/')
api.add_resource(UserDetail, '/<name>')
