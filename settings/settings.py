import json
import os
from pathlib import Path

import boto3
from botocore.client import ClientError

BASE_DIR = Path(__file__).resolve().parent.parent

ENVIRONMENT = os.environ.get("ENVIRONMENT")

SITE_ID = 1

if os.environ.get("SECRETS"):
    SECRETS = json.loads(os.environ.get("SECRETS"))
    del os.environ["SECRETS"]
elif ENVIRONMENT == "development":
    SECRETS = os.environ

SECRET_KEY = SECRETS.get("SECRET_KEY")
DEBUG = ENVIRONMENT == "development" or SECRETS.get("DEBUG", False)

ALLOWED_HOSTS = [
    "localhost",
]

# Application definition
DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "django.contrib.humanize",
]

THIRD_PARTY_APPS = [
    # Rest Framework
    "rest_framework",
    "rest_framework.authtoken",
    # Storage
    "storages",
    # Cors
    "corsheaders",
    # docs
    "drf_spectacular",
    # celery
    "django_celery_beat",
]

PROJECT_APPS = [
    "app.accounts.apps.AccountsConfig",
    "app.core.apps.CoreConfig",
    "app.docs.apps.DocsConfig",
    "app.documents.apps.DocumentsConfig",
]

DEVELOPMENT_APPS = [
    "django_extensions",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

if DEBUG:
    INSTALLED_APPS += DEVELOPMENT_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "settings.urls"

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

WSGI_APPLICATION = "settings.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": SECRETS["DB_NAME"],
        "USER": SECRETS["DB_USER"],
        "PASSWORD": SECRETS["DB_PASSWORD"],
        "HOST": SECRETS["DB_HOST"],
        "PORT": int(SECRETS["DB_PORT"]),
    }
}

# DRF
REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}

SPECTACULAR_SETTINGS = {"PREPROCESSING_HOOKS": ["settings.excluded_path.remove_schema"]}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = "accounts.User"

ROOT_USER = {
    "email": SECRETS.get("ROOT_USER_EMAIL"),
    "password": SECRETS.get("ROOT_USER_PASSWORD"),
}

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


###
# Static Files
###
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static_root")
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
os.makedirs(STATIC_ROOT, exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "static"), exist_ok=True)

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

AWS_S3_REGION_NAME = SECRETS.get("AWS_S3_REGION_NAME", "us-east-2")
AWS_STORAGE_BUCKET_NAME = SECRETS.get("AWS_STORAGE_BUCKET_NAME")
AWS_STORAGE_DATA_BUCKET = SECRETS.get("AWS_STORAGE_DATA_BUCKET")
DEFAULT_BUCKET_URL = f"https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_AUTO_CREATE_BUCKET = True
AWS_IS_GZIPPED = True
AWS_QUERYSTRING_AUTH = True
AWS_S3_ENDPOINT_URL = None
AWS_S3_SIGNATURE_VERSION = "s3v4"

SHARK_DATASET_URL = SECRETS.get("SHARK_DATASET_URL")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "[%(levelname)s] [%(asctime)s] %(name)s.%(funcName)s:%(lineno)s: %(message)s"
        }
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
    },
    "loggers": {
        "app": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}

if DEBUG or ENVIRONMENT == "test":
    DEFAULT_FILE_STORAGE = "app.shared.aws.storage.MinioStorage"

    MINIO_ACCESS_KEY = SECRETS.get("MINIO_ROOT_USER")
    MINIO_SECRET_KEY = SECRETS.get("MINIO_ROOT_PASSWORD")
    MINIO_BUCKET_NAME = SECRETS.get("MINIO_BUCKET_NAME")
    MINIO_ENDPOINT = SECRETS.get("MINIO_ENDPOINT")

    AWS_ACCESS_KEY_ID = MINIO_ACCESS_KEY
    AWS_SECRET_ACCESS_KEY = MINIO_SECRET_KEY
    AWS_STORAGE_BUCKET_NAME = MINIO_BUCKET_NAME
    AWS_S3_ENDPOINT_URL = MINIO_ENDPOINT
    AWS_DEFAULT_ACL = None
    AWS_QUERYSTRING_AUTH = True
    AWS_S3_FILE_OVERWRITE = False

    # s3 = boto3.resource(
    #     "s3",
    #     endpoint_url=AWS_S3_ENDPOINT_URL,
    #     aws_access_key_id=AWS_ACCESS_KEY_ID,
    #     aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    # )
    # try:
    #     s3.meta.client.head_bucket(Bucket=AWS_STORAGE_BUCKET_NAME)
    # except ClientError:
    #     s3.create_bucket(Bucket=AWS_STORAGE_BUCKET_NAME)

    NOTEBOOK_ARGUMENTS = [
        "--allow-root",
        "--ip",
        "0.0.0.0",
        "--port",
        "8888",
        "--no-browser",
        "--NotebookApp.token=''",
        "--NotebookApp.password=''",
    ]
