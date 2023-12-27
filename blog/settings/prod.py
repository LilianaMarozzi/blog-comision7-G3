from .base import *

DEBUG = False   

STATIC_ROOT = BASE_DIR / 'staticfiles'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'gameverseC7G3$blog_db',
        'USER': 'gameverseC7G3',
        'PASSWORD': 'com7grupo3',
        'HOST': 'gameverseC7G3.mysql.pythonanywhere-services.com',
        'PORT': '3306',
    }
}