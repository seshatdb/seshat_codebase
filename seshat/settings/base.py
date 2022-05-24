from pathlib import Path

import os

import django_heroku

import dj_database_url
from decouple import Csv, config

# base_dir is calculated based on this file (base.py) and then goes to parents above.
BASE_DIR = Path(__file__).resolve().parent.parent

#PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

# ==============================================================================
# CORE SETTINGS
# ==============================================================================

SECRET_KEY = config(
    "SECRET_KEY", default="django-insecure$seshat.settings.local")

DEBUG = config("DEBUG", default=True, cast=bool)

#ALLOWED_HOSTS = config("ALLOWED_HOSTS", default="127.0.0.1,localhost", cast=Csv())
ALLOWED_HOSTS = ['seshatdb.herokuapp.com', '127.0.0.1',
                 'majidbenam.com', 'www.majidbenam.com', 'https://majidbenam.com']

INSTALLED_APPS = [
    "seshat.apps.accounts",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",

    'django.contrib.humanize',
    'crispy_forms',
    "seshat.apps.core",
    "seshat.apps.crisisdb",
    "seshat.apps.seshat_api",
    "django_filters",
    "corsheaders",
    "rest_framework",

]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

#ROOT_URLCONF = "urls"
ROOT_URLCONF = "seshat.urls"


INTERNAL_IPS = ["127.0.0.1"]

WSGI_APPLICATION = "seshat.wsgi.application"


# ==============================================================================
# MIDDLEWARE SETTINGS
# ==============================================================================

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",

]


# ==============================================================================
# TEMPLATES SETTINGS
# ==============================================================================

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# ==============================================================================
# DATABASES SETTINGS
# ==============================================================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)
#DATABASES['default'] = dj_database_url.config(conn_max_age=600)

# ==============================================================================
# AUTHENTICATION AND AUTHORIZATION SETTINGS
# ==============================================================================

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


CSRF_TRUSTED_ORIGINS = ['https://majidbenam.com', 'http://*.majidbenam.com', 'http://majidbenam.com',
                        'https://seshatdb.herokuapp.com', 'http://seshatdb.herokuapp.com', 'https://*.majidbenam.com', ]  # the most important one is the last one.

#USE_X_FORWARDED_HOST = True
#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# ==============================================================================
# I18N AND L10N SETTINGS
# ==============================================================================

LANGUAGE_CODE = config("LANGUAGE_CODE", default="en-us")

TIME_ZONE = config("TIME_ZONE", default="UTC")

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = [BASE_DIR / "locale"]

# Email config:
EMAIL_FROM_USER = config('EMAIL_FROM_USER')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
EMAIL_PORT = 587


# ==============================================================================
# STATIC FILES SETTINGS
# ==============================================================================

#STATIC_URL = "/static/"
# this is all browser stuff, what you need to type in the address bar to see the image and stuff
STATIC_URL = "static/"


# this is not needed: the actual value is the default valu:
# /home/majid/dev/seshat/seshat/seshat/staticfiles
# and the files are actually stored there when we COLLECTSTATIC them
STATIC_ROOT = BASE_DIR.parent.parent / "static"

#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

# this one is pretty pointless too
# but let's keep things as it is for the moment
# I believe this says: anything under the base directory that is inside a directory called 'static' will be collected as statidfile,
# regardless of how deep down in the directory hierarchy it might be. It just needs to be a in a older called media in any of the apps, etc.
STATICFILES_DIRS = [BASE_DIR / "static"]


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# We might need to turn these on in production!
# STATICFILES_FINDERS = (
#     "django.contrib.staticfiles.finders.FileSystemFinder",
#     "django.contrib.staticfiles.finders.AppDirectoriesFinder",
# )


# ==============================================================================
# MEDIA FILES SETTINGS
# ==============================================================================

MEDIA_URL = "/media/"

MEDIA_ROOT = BASE_DIR.parent.parent / "media"


# ==============================================================================
# THIRD-PARTY SETTINGS
# ==============================================================================


# ==============================================================================
# FIRST-PARTY SETTINGS
# ==============================================================================

SESHAT_ENVIRONMENT = config("SESHAT_ENVIRONMENT", default="local")


# =================
# Login Redirect
# =================

LOGIN_REDIRECT_URL = 'seshat-index'


# REST Framework
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

# CORS ALLOWED ORIGINS
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000", "http://127.0.0.1:3000",
]

# =================
# Logout Redirect
# =================
#LOGOUT_REDIRECT_URL = 'logout'

# I believe this says: Hey Heroku, do your local settings, don't care about my static_root, static_url etc.
django_heroku.settings(locals())
