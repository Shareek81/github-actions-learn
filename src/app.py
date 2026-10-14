"""A small command-line journal for daily learning notes."""

import argparse
import json
from datetime import date
from pathlib import Path

DEFAULT_STORE = Path.home() / ".commit_buddy.json"


def load_notes(store_path):
    """Return all notes from a JSON file, or an empty list if it is missing."""
    store_path = Path(store_path)
    if not store_path.exists():
        return []
    return json.loads(store_path.read_text(encoding="utf-8"))


def add_note(text, store_path=DEFAULT_STORE):
    """Save a note with today's date and return it."""
    store_path = Path(store_path)
    notes = load_notes(store_path)
    note = {"date": date.today().isoformat(), "text": text}
    notes.append(note)

    store_path.parent.mkdir(parents=True, exist_ok=True)
    store_path.write_text(json.dumps(notes, indent=2) + "\n", encoding="utf-8")
    return note


def main(argv=None):
    parser = argparse.ArgumentParser(description="Save daily Python learning notes.")
    parser.add_argument(
        "--file",
        type=Path,
        default=DEFAULT_STORE,
        help="JSON file used to store notes (default: ~/.commit_buddy.json)",
    )
    commands = parser.add_subparsers(dest="command", required=True)

    add_command = commands.add_parser("add", help="save a note")
    add_command.add_argument("text", help="the note to save")
    commands.add_parser("list", help="show saved notes")

    args = parser.parse_args(argv)
    if args.command == "add":
        note = add_note(args.text, args.file)
        print(f"Saved [{note['date']}]: {note['text']}")
    else:
        notes = load_notes(args.file)
        if not notes:
            print("No notes yet.")
        else:
            for note in notes:
                print(f"[{note['date']}] {note['text']}")


if __name__ == "__main__":
    main()
