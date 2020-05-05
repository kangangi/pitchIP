
class Config:
    '''
    General configuration parent class
    '''
    
    SECRET_KEY = 'Skylar'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'shiksdiana@gmail.com'
    MAIL_PASSWORD = 'Email12345!'



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://diana:12345@localhost/pitcher'
    DEBUG = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://diana:12345@localhost/pitcher_test'


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}