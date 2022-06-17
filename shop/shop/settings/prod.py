import os
import configparser
from .base_settings import *


# SECRET_KEY = 'django-insecure-ps0qq@9+-sg8cd*y+*z#v_l47!ng$y=d1mup6%kx9!x8s%i8mb'
config = configparser.ConfigParser()
config_path = f'{os.getcwd()}/shop/settings/config.ini'
config.read(config_path)
SECRET_KEY = config['SETTINGS']['SECRET_KEY']

DEBUG = False