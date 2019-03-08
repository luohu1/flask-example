from flask import Flask

from config import config


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    from .main import app as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    from .auth import app as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    from .api import app as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api')

    return app
