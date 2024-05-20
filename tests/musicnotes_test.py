import unittest
from musicnotes import note
from unittest.mock import patch

class testnotes(unittest.TestCase):
    @patch('musicnotes.note')
    def test_piano_notes(self, mock_note):
        self.assert_notes_work('piano')

    @patch('musicnotes.note')
    def test_guitar_notes(self, mock_note):
        self.assert_notes_work('guitar')

    def assert_notes_work(self, instrument, mock_note):
        for name in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
            self.assertIsNone(note(name, pitch = 'low', instrument = instrument))
            self.assertIsNone(note(name, pitch = 'mid', instrument = instrument))
            self.assertIsNone(note(name, pitch = 'high', instrument = instrument))

        for name in ['A', 'B', 'D', 'E', 'G']:
            self.assertIsNone(note(name, pitch = 'low', sharp = False, flat = True, instrument = instrument))
            self.assertIsNone(note(name, pitch = 'mid', sharp = False, flat = True, instrument = instrument))
            self.assertIsNone(note(name, pitch = 'high', sharp = False, flat = True, instrument = instrument))

        for name in ['A', 'C', 'D', 'F', 'G']:
            self.assertIsNone(note(name, pitch = 'low', sharp = True, flat = False, instrument = instrument))
            self.assertIsNone(note(name, pitch = 'mid', sharp = True, flat = False, instrument = instrument))
            self.assertIsNone(note(name, pitch = 'high', sharp = True, flat = False, instrument = instrument))

if __name__ == '__main__':
    unittest.main()


