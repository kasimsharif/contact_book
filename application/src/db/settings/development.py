from application.src.db.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'contact_book',
        'USER': 'root',
        'PASSWORD': 'as2d2p',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


