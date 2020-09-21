class Config:
    ENV = 'production'
    DEBUG = False
    SECRET_KEY = 'some-secret-strings'
    JWT_ACCESS_TOKEN_EXPIRES = 86400
    JWT_HEADER_TYPE = 'JWT'


class ProductionConfig(Config):
    ENV = 'production'
    DEBUG = False


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite3'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}