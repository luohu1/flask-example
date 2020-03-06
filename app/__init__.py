import logging

from flask import Blueprint, Flask
from werkzeug.utils import find_modules, import_string

from app.common.errors import register_error_handlers
from app.common.logging import configure_logging
from config import config

logger = logging.getLogger(__name__)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    configure_logging(app)
    register_blueprints(app)
    register_error_handlers(app)

    return app


def register_blueprints(app):
    for name in find_modules('app.views'):
        logger.debug('find modules: %s', name)
        view = import_string(name)
        blueprint = getattr(view, 'app', None)
        if blueprint and isinstance(blueprint, Blueprint):
            app.register_blueprint(blueprint)
