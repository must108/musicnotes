import unittest
from musicnotes import note
from unittest.mock import patch

class testnotes(unittest.TestCase):
    @patch('note')
    def test_piano_notes(self, mock_sound):
        mock_sound.return_value = None
        self.assert_notes_return_none('piano', mock_sound)

    @patch('note')
    def test_guitar_notes(self, mock_sound):
        mock_sound.return_value = None
        self.assert_notes_return_none('guitar', mock_sound)

    def assert_notes_return_none(self, instrument, mock_sound):
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


