# coding: utf-8
from flask import jsonify
from flask_jwt_extended import get_raw_jwt, jwt_required
from flask_restful import Resource


class Token(Resource):
    @jwt_required
    def get(self):
        token = get_raw_jwt()
        return jsonify(token=token)
