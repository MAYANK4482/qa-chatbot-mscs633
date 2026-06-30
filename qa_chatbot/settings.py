"""Django settings for the qa_chatbot project (MSCS-633 Hands-On Assignment 3)."""

from __future__ import annotations

import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "mscs633-dev-only-not-a-secret")

DEBUG = True
ALLOWED_HOSTS: list[str] = []

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "chatterbot.ext.django_chatterbot",
    "assistant",
]

ROOT_URLCONF = "qa_chatbot.urls"
WSGI_APPLICATION = "qa_chatbot.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

CHATTERBOT = {
    "name": "TerminalBot",
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
