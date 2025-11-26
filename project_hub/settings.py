"""
Django settings for project_hub project.
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------------------------
# ENVIRONMENT
# -------------------------------------------------
ENVIRONMENT = os.environ.get("ENVIRONMENT", "development")

# -------------------------------------------------
# SECURITY
# -------------------------------------------------
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-insecure-secret-key")
DEBUG = ENVIRONMENT == "development"

ALLOWED_HOSTS = [
    "127.0.0.1",
    "localhost",
    "sokiyan.ir",
    ".sokiyan.ir",
    "www.sokiyan.ir",
    ".onrender.com",
]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")


# -------------------------------------------------
# STATIC FILES
# -------------------------------------------------
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


# -------------------------------------------------
# MEDIA FILES (Cloudinary in Production)
# -------------------------------------------------
if ENVIRONMENT == "development":
    MEDIA_URL = "/media/"
    MEDIA_ROOT = BASE_DIR / "media"
    DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"

else:
    import cloudinary
    import cloudinary_storage.storage

    cloudinary.config(
        cloud_name=os.environ.get("CLOUDINARY_CLOUD_NAME"),
        api_key=os.environ.get("CLOUDINARY_API_KEY"),
        api_secret=os.environ.get("CLOUDINARY_API_SECRET"),
        secure=True,
    )

    DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
    MEDIA_URL = "/media/"  # Cloudinary doesn’t use this but Django needs it

    CLOUDINARY_CLOUD_NAME = os.environ.get("CLOUDINARY_CLOUD_NAME")
    CLOUDINARY_URL = f"cloudinary://{os.environ.get('CLOUDINARY_API_KEY')}:{os.environ.get('CLOUDINARY_API_SECRET')}@{CLOUDINARY_CLOUD_NAME}"


# -------------------------------------------------
# APPS
# -------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Your apps
    "home",
    "service",
    "contact",

    # Cloudinary
    "cloudinary",
    "cloudinary_storage",
]


# -------------------------------------------------
# MIDDLEWARE
# -------------------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


# -------------------------------------------------
# URL & WSGI
# -------------------------------------------------
ROOT_URLCONF = "project_hub.urls"
WSGI_APPLICATION = "project_hub.wsgi.application"


# -------------------------------------------------
# TEMPLATES
# -------------------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# -------------------------------------------------
# DATABASE
# -------------------------------------------------
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# -------------------------------------------------
# AUTH PASSWORD VALIDATORS
# -------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# -------------------------------------------------
# INTERNATIONALIZATION
# -------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True


# -------------------------------------------------
# EMAIL
# -------------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = "soheil.ce.99@gmail.com"
EMAIL_HOST_PASSWORD = "eynb rjeo pkxo cdrg"
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
