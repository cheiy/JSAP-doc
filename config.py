#config.py

class Config(object):
    """
    Common configurations
    """

class DevelopmentConfig(Config):
    """
    Development configurations
    """

    DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Production configs
    """
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
    }
