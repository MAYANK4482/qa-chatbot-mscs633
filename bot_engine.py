"""Shared ChatterBot engine for the MSCS-633 Q&A chatbot.

Reused by both the standalone client (chatbot.py) and the Django management
command (manage.py chat). Imports nothing from Django.

Course : 2026 Summer - Advanced Artificial Intelligence (MSCS-633-M50)
Author : Mayank Vadaliya
"""

from __future__ import annotations

import logging
from typing import Iterable, Sequence

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

DEFAULT_BOT_NAME = "TerminalBot"
DEFAULT_DATABASE_URI = "sqlite:///database.sqlite3"
DEFAULT_LOGIC_ADAPTERS = ("chatterbot.logic.BestMatch",)
DEFAULT_CORPORA: tuple[str, ...] = (
    "chatterbot.corpus.english.greetings",
    "chatterbot.corpus.english.conversations",
)
EXIT_KEYWORDS = frozenset({"exit", "quit", "bye", "goodbye"})

logger = logging.getLogger(__name__)


def build_chatbot(
    name: str = DEFAULT_BOT_NAME,
    *,
    storage_adapter: str = "chatterbot.storage.SQLStorageAdapter",
    database_uri: str | None = DEFAULT_DATABASE_URI,
    logic_adapters: Sequence[str] = DEFAULT_LOGIC_ADAPTERS,
    read_only: bool = False,
) -> ChatBot:
    """Construct and return a configured ChatBot."""
    kwargs: dict = {
        "storage_adapter": storage_adapter,
        "logic_adapters": list(logic_adapters),
        "read_only": read_only,
    }
    if database_uri is not None:
        kwargs["database_uri"] = database_uri
    return ChatBot(name, **kwargs)


def is_trained(chatbot: ChatBot) -> bool:
    """Return True if the bot's storage already holds learned statements."""
    try:
        return chatbot.storage.count() > 0
    except Exception:
        return False


def train_chatbot(
    chatbot: ChatBot,
    corpora: Iterable[str] = DEFAULT_CORPORA,
    *,
    force: bool = False,
) -> bool:
    """Train the bot on the given corpora; skip if already trained."""
    if not force and is_trained(chatbot):
        logger.info("Bot already trained - skipping.")
        return False
    trainer = ChatterBotCorpusTrainer(chatbot)
    trainer.train(*corpora)
    return True


def get_reply(chatbot: ChatBot, message: str) -> str:
    """Return the bot's textual response to a single message."""
    return str(chatbot.get_response(message))


def run_chat_loop(
    chatbot: ChatBot,
    *,
    user_label: str = "user",
    bot_label: str = "bot",
    show_banner: bool = True,
) -> None:
    """Run the interactive terminal user:/bot: loop."""
    if show_banner:
        print("=" * 60)
        print(f"  {chatbot.name} - Simple Q&A Chatbot (MSCS-633)")
        print("  Type a message and press Enter. Type 'exit' to quit.")
        print("=" * 60)

    while True:
        try:
            message = input(f"{user_label}: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            print(f"{bot_label}: Goodbye!")
            break
        if not message:
            continue
        if message.lower() in EXIT_KEYWORDS:
            print(f"{bot_label}: Goodbye!")
            break
        print(f"{bot_label}: {get_reply(chatbot, message)}")
