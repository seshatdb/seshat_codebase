from pathlib import Path

import os

import django_heroku

import dj_database_url
from decouple import Csv, config

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
                 'majidbenam.com', 'www.majidbenam.com']

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
    "django_filters",
    "corsheaders",

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
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "corsheaders.middleware.CorsMiddleware",
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


CSRF_TRUSTED_ORIGINS = ['https://majidbenam.com', 'http://*.majidbenam.com', 'http://majidbenam.com', 'www.majidbenam.com',
                        'https://seshatdb.herokuapp.com', 'http://seshatdb.herokuapp.com', 'www.seshatdb.herokuapp.com', 'https://*.majidbenam.com', ]  # the most important one is the last one.

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


# ==============================================================================
# STATIC FILES SETTINGS
# ==============================================================================

#STATIC_URL = "/static/"
STATIC_URL = "static/"


STATIC_ROOT = BASE_DIR.parent.parent / "static"
#STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')

STATICFILES_DIRS = [BASE_DIR / "static"]


STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


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

# =================
# Logout Redirect
# =================
#LOGOUT_REDIRECT_URL = 'logout'

django_heroku.settings(locals())
