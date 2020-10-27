import os

class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = 'TheDifference'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wambui:neema@localhost/pitches'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587 
    MAIL_USE_TLS = True
    MAIL_USERNAME ='pwambui13@gmail.com'
    MAIL_PASSWORD = 'laurenneema'
    SUBJECT_PREFIX = 'One Minute Pitch'
    SENDER_EMAIL = 'pwambui13@gmail.com'

    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wambui:neema@localhost/pitch_test'


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    
class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}