from application.src.db.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'contact_book',
        'USER': 'root',
        'PASSWORD': 'as2d2',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


