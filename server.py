from app import app

import config

if __name__ == '__main__':
    app.config.from_object(config.DevelopmentConfig)
    app.run()
