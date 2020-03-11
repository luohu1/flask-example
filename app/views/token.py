# coding: utf-8
from flask import Blueprint, jsonify, request
from flask_jwt_extended import (decode_token, get_jwt_identity, get_raw_jwt,
                                jwt_required)
from flask_restful import Api, Resource

app = Blueprint('token', __name__, url_prefix='/tokens')
api = Api(app)


class Token(Resource):
    @jwt_required
    def get(self):
        token = get_raw_jwt()
        return jsonify(token=token)


api.add_resource(Token, '/')
