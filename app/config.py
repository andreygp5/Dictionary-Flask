import os
from dotenv import load_dotenv


path = os.path.dirname(__file__)
dotenv_path = os.path.join(path, '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

class Config:
    DEBUG = "True"
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')