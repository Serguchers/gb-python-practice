from re import I
from .base_settings import *

SECRET_KEY = 'django-insecure-ps0qq@9+-sg8cd*y+*z#v_l47!ng$y=d1mup6%kx9!x8s%i8mb'

DEBUG = True

SITE_ID = 1

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'shop',
        'USER': 'sergei',
        'PASSWORD': 'qwerty',
        'HOST': 'db',
        'PORT': '5432',
    }
}