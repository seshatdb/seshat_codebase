# flake8: noqa

from .base import *

INSTALLED_APPS += ["debug_toolbar"]

#MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")


# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': '',
    }
}

# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
