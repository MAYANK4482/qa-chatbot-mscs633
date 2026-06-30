# Simple Q&A Chatbot (MSCS-633, Summer 2026)

A terminal chatbot built with **Python**, **Django**, and **ChatterBot**. Built as the Hands-On Assignment 3 deliverable for **MSCS-633 — Advanced Artificial Intelligence** at the University of the Cumberlands.

> **ChatterBot** is a machine-learning-based conversational dialog engine. It generates a reply by comparing your input against a corpus of known conversations and returning the response associated with the closest match. The more it is trained, the better its matches become.

---

## Two ways to run the same bot

The conversational logic lives in one shared module (`bot_engine.py`) and is exposed through two front ends:

| Front end | Command | Storage backend |
|---|---|---|
| **Standalone Python** | `python chatbot.py` | SQLite via ChatterBot's `SQLStorageAdapter` |
| **Django management command** | `python manage.py chat` | Django ORM via ChatterBot's `DjangoStorageAdapter` |

Both train on the bundled English corpus and present the exact `user:` / `bot:` terminal format from the assignment brief.

---

## Features

- ✅ **Trained on the English corpus** (greetings + conversations) via `ChatterBotCorpusTrainer`
- ✅ **Shared engine, two entry points** — no duplicated logic between the script and the Django command (DRY)
- ✅ **Idempotent training** — retrains only on a fresh database; `--retrain` forces it
- ✅ **Graceful exit** — `exit`/`quit`/`bye`, plus `Ctrl-C` and `Ctrl-D` are all handled
- ✅ **Configurable** — bot name, database URI, read-only mode exposed via flags
- ✅ **Fully documented** — module + function docstrings, type hints, and inline rationale

---

## Requirements

- Python **3.10–3.14** (developed and tested on 3.12.3)
- macOS, Linux, or Windows

---

## Installation

```bash
git clone https://github.com/MAYANK4482/qa-chatbot-mscs633.git
cd qa-chatbot-mscs633

python3 -m venv .venv
source .venv/bin/activate           # Windows: .venv\Scripts\activate

pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

> **Why the extra `spacy download` step?** ChatterBot 1.2.x uses spaCy for
> part-of-speech tagging and lemmatization, and spaCy needs its English model
> (`en_core_web_sm`) installed separately. If you skip it you will get a
> `ChatBotException: The Spacy model for "English" language is missing.`

---

## Usage

### Option A — Standalone (simplest)

```bash
python chatbot.py
```

Optional flags:

```bash
python chatbot.py --name HelpBot --database "sqlite:///mybot.sqlite3"
python chatbot.py --retrain        # force retraining on the corpus
python chatbot.py --read-only      # don't learn from the human's inputs
```

### Option B — Through Django

```bash
python manage.py migrate           # one-time: creates the chatterbot tables
python manage.py chat              # start chatting
python manage.py chat --retrain    # force retraining
```

---

## Sample Session

This is a real transcript captured from `python chatbot.py`:

```text
============================================================
  TerminalBot - Simple Q&A Chatbot (MSCS-633)
  Type a message and press Enter. Type 'exit' to quit.
============================================================
user: Good morning! How are you doing?
bot: I am doing well, how about you?
user: You're welcome.
bot: What is it like?
user: What is your name?
bot: Could I borrow a cup of sugar?
user: exit
bot: Goodbye!
```

> Replies are drawn from ChatterBot's English corpus, so a small training set
> occasionally produces an off-topic answer — that is expected behaviour for a
> nearest-match dialog engine and improves as the corpus grows.

---

## Author

**Mayank Vadaliya** — doctoral researcher in Information Technology, University of the Cumberlands
ORCID: [0009-0008-0320-6131](https://orcid.org/0009-0008-0320-6131)
Course: MSCS-633-M50 — Advanced Artificial Intelligence (Summer 2026)
