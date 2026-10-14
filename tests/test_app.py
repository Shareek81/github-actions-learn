import tempfile
import unittest
from pathlib import Path

from src.app import add_note, load_notes


class NotesTests(unittest.TestCase):
    def test_missing_file_has_no_notes(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            store_path = Path(temporary_directory) / "notes.json"
            self.assertEqual(load_notes(store_path), [])

    def test_add_note_saves_and_returns_note(self):
        with tempfile.TemporaryDirectory() as temporary_directory:
            store_path = Path(temporary_directory) / "notes.json"

            note = add_note("Practice GitHub Actions", store_path)

            self.assertEqual(note["text"], "Practice GitHub Actions")
            self.assertEqual(load_notes(store_path), [note])
            self.assertEqual(len(note["date"]), 10)


if __name__ == "__main__":
    unittest.main()
