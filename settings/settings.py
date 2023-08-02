import json
import os

from pathlib import Path

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
    "app.core.apps.CoreConfig",
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'settings.wsgi.application'


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


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

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
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

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

if DEBUG or ENVIRONMENT == "test":
    MINIO_ACCESS_KEY = os.getenv("MINIO_ROOT_USER")
    MINIO_SECRET_KEY = os.getenv("MINIO_ROOT_PASSWORD")
    MINIO_BUCKET_NAME = os.getenv("MINIO_BUCKET_NAME")
    MINIO_ENDPOINT = os.getenv("MINIO_ENDPOINT")

    AWS_ACCESS_KEY_ID = MINIO_ACCESS_KEY
    AWS_SECRET_ACCESS_KEY = MINIO_SECRET_KEY
    AWS_STORAGE_BUCKET_NAME = MINIO_BUCKET_NAME
    AWS_S3_ENDPOINT_URL = MINIO_ENDPOINT
    AWS_DEFAULT_ACL = None
    AWS_QUERYSTRING_AUTH = True
    AWS_S3_FILE_OVERWRITE = False
