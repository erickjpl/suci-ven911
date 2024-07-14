"""
Django settings for suci project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

import os
from pathlib import Path

# from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = "django-insecure-t#&s(2=)83@)v9@8$5eok0)e@r$zzz3m4nw*3^1e9(*e0oloef"
SECRET_KEY = os.environ.get("SECRET_KEY", default="django-insecure-t#&s(2=)83@)v9@8$5eok0)e@r$zzz3m4nw*3^1e9(*e0oloef")


# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = os.environ.get("DEBUG", "True").lower() in ["true", "yes", "1"]

ALLOWED_HOSTS = ["*"]

CSRF_ALLOWED_ORIGINS = [os.environ.get("BASE_URL", default="http://127.0.0.1")]
CSRF_TRUSTED_ORIGINS = [os.environ.get("BASE_URL", default="http://127.0.0.1")]
CSRF_COOKIE_SECURE = os.environ.get("CSRF_COOKIE_SECURE", default="True")

CORS_ORIGINS_WHITELIST = [os.environ.get("BASE_URL", default="http://127.0.0.1")]
CORS_ALLOWED_ORIGINS = [os.environ.get("BASE_URL", default="http://127.0.0.1")]

# Current DJANGO_ENVIRONMENT
ENVIRONMENT = os.environ.get("DJANGO_ENVIRONMENT", default="local")

INTERNAL_IPS = ["127.0.0.1", "::1"]


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "organizacion",
    "presupuesto",
    "index",
    "paneluser",
    "biblioteca",
    "seguridad",
    "planificacion",
    "emergencia",
    "potencia",
    "asesoria",
    "rrhh",
    "uri",
    "emergency",
    "gestion_comunicacional",
    "administracion",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "suci.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

WSGI_APPLICATION = "suci.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

if os.environ.get("DB_BACKEND").lower() == "postgresql":
    # See docs/contributing for instructions on configuring PostgreSQL.
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("DB_BACKEND", default="suci_ven911").lower(),
            "USER": os.environ.get("DB_BACKEND", default="suci").lower(),
            "PASSWORD": os.environ.get("DB_BACKEND", default="123456").lower(),
        }
    }
if os.environ.get("DB_BACKEND").lower() == "mysql":
    # See docs/contributing for instructions on configuring MySQL/MariaDB.
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": os.environ.get("DB_BACKEND", default="suci_ven911").lower(),
            "USER": os.environ.get("DB_BACKEND", default="suci").lower(),
            "PASSWORD": os.environ.get("DB_BACKEND", default="123456").lower(),
        }
    }

if os.environ.get("DB_BACKEND", default="sqlite").lower() == "sqlite":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = "es-ES"

TIME_ZONE = "America/Caracas"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# MEDIA_ROOT = BASE_DIR / 'media'

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


MEDIA_ROOT = os.path.join(BASE_DIR, "media").replace("\\", "/")
MEDIA_URL = "/media/"

# CSRF_TRUSTED_ORIGINS = ["https://19d7-150-188-246-2.ngrok-free.app/"]

AUTH_USER_MODEL = "paneluser.Usuarios"
