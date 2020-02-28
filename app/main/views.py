import logging

from flask import render_template

from . import app

logger = logging.getLogger(__name__)

@app.route('/')
def index():
    logger.info('index')
    return render_template('index.html', content="Hello World")
