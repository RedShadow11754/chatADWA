import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()               # safe: reads .env locally; Render will use env vars

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-for-local")
DEBUG = os.getenv("DEBUG", "False").lower() in ("1", "true", "yes")

# Hosts
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "").split(",") if os.getenv("ALLOWED_HOSTS") else ["localhost", "127.0.0.1"]

# Timezone / i18n
LANGUAGE_CODE = "en-us"
TIME_ZONE = os.getenv("TIME_ZONE", "Africa/Addis_Ababa")   # change if you prefer UTC
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

# Middleware: cors should be high; whitenoise after SecurityMiddleware
MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",                # keep early
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# URL / WSGI - ensure these names match your project folder/module
ROOT_URLCONF = "project_adwa.urls"        # <-- ensure this matches your folder (project_adwa or Project_Adwa)
WSGI_APPLICATION = "project_adwa.wsgi.application"

# Database: prefer DATABASE_URL in production; fallback to sqlite for local dev
import dj_database_url   # add to requirements if you use it
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(DATABASE_URL, conn_max_age=600)
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Static files (for collectstatic on Render)
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_DIRS = [BASE_DIR / "static"]   # optional: if you keep a top-level static folder
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# CORS (dev defaults)
CORS_ALLOWED_ORIGINS = os.getenv("CORS_ALLOWED_ORIGINS", "http://localhost:5173,http://127.0.0.1:5173").split(",")

# Other helpful defaults
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"