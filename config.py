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


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}