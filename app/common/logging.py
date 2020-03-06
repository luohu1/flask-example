# coding: utf-8
import logging
import sys

from flask.logging import default_handler

default_formatter = '%(asctime)s %(process)d,%(threadName)s %(filename)s:%(lineno)d [%(levelname)s] %(message)s'


def configure_logging(app):
    # handler = None
    if app.debug:
        handler = logging.StreamHandler(sys.stdout)
    else:
        filename = app.config['LOGFILE']
        handler = logging.handlers.TimedRotatingFileHandler(filename, when='D')

    handler.setLevel(logging.INFO)
    handler.setFormatter(logging.Formatter(default_formatter))
    app.logger.addHandler(handler)
    app.logger.removeHandler(default_handler)
