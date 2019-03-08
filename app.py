from flask import Flask, render_template

import config

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', content="Hello World")


if __name__ == '__main__':
    app.config.from_object(config.DevelopmentConfig)
    app.run()
