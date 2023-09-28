import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-7bqf4zndoah$s&cpnmhvc=yt*cw39*)qxjr^1jxi1*i)-_9(zi"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG')

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_BASE = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

INSTALLED_THRIDS = [
    "rest_framework",
    "drf_spectacular",
    "corsheaders",
    "rest_framework_simplejwt",
]
INSTALLED_LOCAL = [
    "core.products",
    "core.sales",
    "core.users",
    "core.orders",
    "core.company",
]
INSTALLED_APPS = INSTALLED_BASE + INSTALLED_LOCAL + INSTALLED_THRIDS

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "quickBillBackend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
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

WSGI_APPLICATION = "quickBillBackend.wsgi.application"





# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_URL = "/static/"
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
# MEDIA_URL = "/media/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media")


if DEBUG:

    # Database
    # https://docs.djangoproject.com/en/4.1/ref/settings/#databases

    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

    ########################### DEV ##################################

    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        BASE_DIR / "static",
    ]


    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

else:

    # Database
    # https://docs.djangoproject.com/en/4.1/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('NAMEDB'),
            'USER': os.getenv('USERDB'),
            'PASSWORD': os.getenv('PASSWORDDB'),
            'HOST': os.getenv('HOSTDB'),
            'PORT': os.getenv('PORTDB'),
        }
    }
############################ PRO #################################
    STATIC_URL = '/static/'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

#############################################################

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# EMAIL CONFIG

EMAIL_BACKEND =os.getenv('EMAIL_BACKEND')
EMAIL_HOST =os.getenv('EMAIL_HOST')
EMAIL_PORT =os.getenv('EMAIL_PORT')
EMAIL_HOST_USER =os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD =os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS =os.getenv('EMAIL_USE_TLS')

# user model
AUTH_USER_MODEL = "users.Users"

# API
REST_FRAMEWORK = {
    # YOUR SETTINGS
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=1),
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Quick Bill API",
    "DESCRIPTION": "The API provides a platform for managing product, user, and sales information for an online store. Users can perform CRUD operations (create, read, update, and delete) on the data, as well as view reports and analytics on sales performance. The API is designed to be flexible and scalable, supporting a wide range of use cases and integration scenarios. With its intuitive and robust interface, the API makes it easy to manage and optimize your online store, empowering you to drive growth and profitability.",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}

# cors origin
CORS_ORIGIN_WHITELIST = ["http://localhost:5173"]
