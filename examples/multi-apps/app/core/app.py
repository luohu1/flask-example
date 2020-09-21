# coding: utf-8
import logging

from flask import Blueprint

logger = logging.getLogger(__name__)

app = Blueprint('core', __name__)


@app.route('/', methods=["GET"])
def index():
    logger.info('/index')
    return "Hello World."
