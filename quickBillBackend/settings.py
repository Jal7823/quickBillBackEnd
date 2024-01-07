import os
from dotenv import load_dotenv
from pathlib import Path
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG')

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
    "apps.products",
    "apps.sales",
    "apps.users",
    "apps.company",
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

    ALLOWED_HOSTS = ['*']

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

    ALLOWED_HOSTS = ['haroburges.pythonanywhere.com']

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': os.getenv('NAMEDB'),
            'USER': os.getenv('USERDB'),
            'PASSWORD': os.getenv('PASSWORDB'),
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

# EMAIL_BACKEND = os.getenv('EMAIL_BACKEND')
# EMAIL_HOST = os.getenv('EMAIL_HOST')
# EMAIL_PORT = os.getenv('EMAIL_PORT')
# EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
# EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
# EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS')

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
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Quick Bill API",
    "CONTACT": {
        "name": "Jalberth M.",
        "email": "jal7823@gmail.com",
        "url": "https://jal7823.github.io/newPortFolio2023FrontEnd",
    },
    "DESCRIPTION": """
    
    The API provides a platform for managing product, user, and sales information for an online store. Users can perform CRUD operations (create, read, update, and delete) on the data, as well as view reports and analytics on sales performance. The API is designed to be flexible and scalable, supporting a wide range of use cases and integration scenarios. With its intuitive and robust interface, the API makes it easy to manage and optimize your online store, empowering you to drive growth and profitability.
    
    ⚠️ The API have implemented JWT, so you need get a token in the corresponding endpoint (token) and authenticate for complete use of this api
    
     You should use two users:
     - clients
     - employee
    
     Both users have a different permission access to different endpoints, that with the finally to protected the sensitive information
 
     ⚠️ Since this project is for demonstration only, the queries per user will be limited to 5 per user (customer, employee).
    
    """

    ,
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,

    "SWAGGER_UI_SETTINGS": {
        'docExpansion': None
    },
    "SECURITY_DEFINITIONS": {
        "Bearer Token": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
        },
    },
    'DEFAULT_THROTTLE_RATES': {
        'user': '5/month',
    },
    "EXTERNAL_DOCS": {
        "description": "GitHub",
        "url": "https://github.com/Jal7823/quickBillBackEnd",
    }
}

# cors origin
CORS_ORIGIN_WHITELIST = ["http://localhost:5173"]
