"""Django's command-line utility for administrative tasks.

Run the chatbot through Django with:

    python manage.py migrate      # create the chatterbot tables (first run only)
    python manage.py chat         # start the terminal Q&A chat
"""

import os
import sys


def main() -> None:
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qa_chatbot.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
