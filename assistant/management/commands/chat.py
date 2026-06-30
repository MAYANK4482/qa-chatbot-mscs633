"""python manage.py chat - run the Q&A chatbot inside Django (Django ORM storage)."""

from __future__ import annotations

from django.core.management.base import BaseCommand

from bot_engine import build_chatbot, run_chat_loop, train_chatbot


class Command(BaseCommand):
    help = "Start an interactive terminal Q&A chat using ChatterBot + Django."

    def add_arguments(self, parser) -> None:
        parser.add_argument("--retrain", action="store_true",
                            help="Force retraining on the English corpus even if already trained.")
        parser.add_argument("--read-only", action="store_true",
                            help="Do not let the bot learn from your messages during the chat.")

    def handle(self, *args, **options) -> None:
        chatbot = build_chatbot(
            "TerminalBot",
            storage_adapter="chatterbot.storage.DjangoStorageAdapter",
            database_uri=None,
            read_only=options["read_only"],
        )
        self.stdout.write("Preparing the bot (first-run training can take a few seconds)...")
        trained = train_chatbot(chatbot, force=options["retrain"])
        self.stdout.write(
            self.style.SUCCESS("Training complete.")
            if trained else "Already trained - skipping training."
        )
        run_chat_loop(chatbot)
