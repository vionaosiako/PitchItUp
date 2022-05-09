import os

class Config:
    # SECRET_KEY='vivioonana123'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://riziki:riziki@localhost/pitches'

class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}