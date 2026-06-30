"""Standalone terminal Q&A chatbot.

Run with: python chatbot.py
Conversational logic lives in bot_engine.py (shared with manage.py chat).

Course : 2026 Summer - Advanced Artificial Intelligence (MSCS-633-M50)
Author : Mayank Vadaliya
"""

from __future__ import annotations

import argparse

from bot_engine import (
    DEFAULT_BOT_NAME,
    DEFAULT_DATABASE_URI,
    build_chatbot,
    run_chat_loop,
    train_chatbot,
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    """Define and parse the command-line interface."""
    parser = argparse.ArgumentParser(
        prog="chatbot",
        description="A simple Q&A chatbot built with Python and ChatterBot.",
        epilog="Type 'exit' (or press Ctrl-D) inside the chat to quit.",
    )
    parser.add_argument("--name", default=DEFAULT_BOT_NAME,
                        help=f"Display name for the bot (default: {DEFAULT_BOT_NAME}).")
    parser.add_argument("--database", default=DEFAULT_DATABASE_URI,
                        help=f"SQLAlchemy database URI (default: {DEFAULT_DATABASE_URI}).")
    parser.add_argument("--retrain", action="store_true",
                        help="Force retraining on the English corpus even if already trained.")
    parser.add_argument("--read-only", action="store_true",
                        help="Do not let the bot learn from your messages during the chat.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    """Build, train (if needed), and run the chatbot."""
    args = parse_args(argv)
    chatbot = build_chatbot(args.name, database_uri=args.database, read_only=args.read_only)
    print("Preparing the bot (training on first run may take a few seconds)...")
    trained = train_chatbot(chatbot, force=args.retrain)
    print("Training complete." if trained else "Already trained - skipping training.")
    run_chat_loop(chatbot)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
