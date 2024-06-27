from os import environ
import secrets

# Generate a URL-safe text string
secret_key = secrets.token_urlsafe(32)


class Config:
    ####### Application Configs #######
    ENV = environ.get("CHIRPVERSE_CCS_ENV", "production")
    DEBUG = bool(int(environ.get("CHIRPVERSE_CCS_DEBUG", "0")))
    TESTING = bool(int(environ.get("CHIRPVERSE_CCS_TESTING", "0")))
    SECRET_KEY = secret_key
    ####### Database Configs ########
    SQLALCHEMY_DATABASE_URI = environ.get('CHIRPVERSE_CCS_DATABASE_URI', None)
    SQLALCHEMY_TRACK_MODIFICATIONS = DEBUG
    SQLALCHEMY_ECHO = DEBUG
    SQLALCHEMY_RECORD_QUERIES = DEBUG
