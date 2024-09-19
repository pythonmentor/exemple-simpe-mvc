import secrets
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Configuration minimale pour Django ORM
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "library.db",
    }
}

INSTALLED_APPS = [
    "library",
]

SECRET_KEY = secrets.token_urlsafe(64)
DEBUG = True
