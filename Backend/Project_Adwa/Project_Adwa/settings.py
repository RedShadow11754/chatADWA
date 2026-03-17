import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # safe: reads .env locally; Render will use env vars

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-for-local")
DEBUG = os.getenv("DEBUG", "False").lower() in ("1", "true", "yes")

# Hosts
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",") if os.getenv("ALLOWED_HOSTS") else ["localhost", "127.0.0.1"]

# Timezone / i18n
LANGUAGE_CODE = "en-us"
TIME_ZONE = os.getenv("TIME_ZONE", "Africa/Addis_Ababa")
USE_I18N = True
USE_TZ = True

# Apps
INSTALLED_APPS = [
    "corsheaders",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "adwa_app",
]

# Middleware
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URL / WSGI
ROOT_URLCONF = "Project_Adwa.urls"
WSGI_APPLICATION = "Project_Adwa.wsgi.application"


# Database: dummy SQLite fallback (not used if you rely on Chroma)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Static files
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]  # optional
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# CORS
CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173").split(",")

# Other defaults
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
