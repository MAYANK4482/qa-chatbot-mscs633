"""App configuration for the assistant Django app."""

from __future__ import annotations

from django.apps import AppConfig


class AssistantConfig(AppConfig):
    default_auto_field = "django.db.models.AutoField"
    name = "assistant"
    verbose_name = "Q&A Chatbot Assistant"
