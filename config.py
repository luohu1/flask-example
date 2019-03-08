class Config:
    pass


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