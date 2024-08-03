import os

from django.conf.global_settings import CACHES


from .base import *
import logging

DEBUG=False
CSRF_COOKIE_SECURE=True
SESSION_COOKIE_SECURE=True
SECURE_SSL_REDIRECT=True

ADMINS=[
    ('Pastor Gar','gar.shalom1@gmail.com'),
    ('Eleazer','femmanalis95@gmail.com'),
]

ALLOWED_HOSTS=['*']

DATABASES={
    'default':{
        'ENGINE':'django.db.backends.postgresql',
        'NAME':os.environ.get('POSTGRES_DB'),
        'USER':os.environ.get('POSTGRES_USER'),
        'PASSWORD':os.environ.get('POSTGRES_PASSWORD'),
        'HOST':'db',
        'PORT':5432,
    }
}

REDIS_URL='redis://cache:6379'
CACHES['default']['LOCATION']=REDIS_URL
CHANNEL_LAYERS['default']['CONFIG']['hosts']=[REDIS_URL]