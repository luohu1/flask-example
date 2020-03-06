# coding: utf-8
import logging

from flask import Blueprint
from flask_restful import Api, Resource

logger = logging.getLogger(__name__)

app = Blueprint('index', __name__)
api = Api(app)


class Index(Resource):
    def get(self):
        logger.info('index')
        return "Index"


api.add_resource(Index, '/')
