import tempfile
import unittest
from pathlib import Path

from src.app import add_note, load_notes, is_odd


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

    def test_is_odd_for_odd_value(self):
        res = is_odd(3)
        self.assertTrue(res)

    def test_is_odd_for_even_value(self):
        res = is_odd(6)
        self.assertFalse(res)

    def test_is_odd_for_zero(self):
        res = is_odd(0)
        self.assertFalse(res)


if __name__ == "__main__":
    unittest.main()
