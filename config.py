import os

class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://<username>:<password>@localhost/<db_name>'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
