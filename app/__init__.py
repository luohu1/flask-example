import logging

from flask import Blueprint, Flask
from werkzeug.utils import import_string

from app.common.errors import register_error_handlers
from app.common.logging import configure_logging
from app.extentions import jwt, db
from config import config

logger = logging.getLogger(__name__)


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    configure_logging(app)
    register_extentions(app)
    register_error_handlers(app)

    register_blueprints(app, ['core', 'users'])

    return app


def register_extentions(app):
    jwt.init_app(app)
    db.init_app(app)


def register_blueprints(app, blueprints, prefix='app'):
    for blueprint in blueprints:
        module_string = '.'.join([prefix, blueprint, 'app'])
        try:
            module = import_string(module_string)
        except Exception:
            logger.error('module: {} can not import.'.format(module_string))
            continue
        blueprint_obj = getattr(module, 'app', None)
        if blueprint_obj and isinstance(blueprint_obj, Blueprint):
            app.register_blueprint(blueprint_obj)
        else:
            logger.error('can not load blueprint {}'.format(blueprint))
