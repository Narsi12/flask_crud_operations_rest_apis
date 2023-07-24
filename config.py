import os

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:root@localhost/crud_flask'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
