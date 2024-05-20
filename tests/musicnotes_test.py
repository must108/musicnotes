import unittest
from musicnotes import note
from unittest.mock import patch

class testnotes(unittest.TestCase):
    @patch('musicnotes.note')
    def test_piano_notes(self, mock_note):
        self.assert_notes_return_correctly('piano', mock_note)

    @patch('musicnotes.note')
    def test_guitar_notes(self, mock_note):
        self.assert_notes_return_correctly('guitar', mock_note)

    def assert_notes_called_correctly(self, instrument, mock_note):
            note_names = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

            # Test without sharp or flat
            for name in note_names:
                with self.subTest(name=name, pitch='low'):
                    note(name, pitch='low', instrument=instrument)
                    mock_note.assert_called_with(name, pitch='low', instrument=instrument)
                
                with self.subTest(name=name, pitch='mid'):
                    note(name, pitch='mid', instrument=instrument)
                    mock_note.assert_called_with(name, pitch='mid', instrument=instrument)
                
                with self.subTest(name=name, pitch='high'):
                    note(name, pitch='high', instrument=instrument)
                    mock_note.assert_called_with(name, pitch='high', instrument=instrument)

            # Test flat notes
            flat_note_names = ['A', 'B', 'D', 'E', 'G']
            for name in flat_note_names:
                with self.subTest(name=name, pitch='low', flat=True):
                    note(name, pitch='low', sharp=False, flat=True, instrument=instrument)
                    mock_note.assert_called_with(name, pitch='low', sharp=False, flat=True, instrument=instrument)
                
                with self.subTest(name=name, pitch='mid', flat=True):
                    note(name, pitch='mid', sharp=False, flat=True, instrument=instrument)
                    mock_note.assert_called_with(name, pitch='mid', sharp=False, flat=True, instrument=instrument)
                
                with self.subTest(name=name, pitch='high', flat=True):
                    note(name, pitch='high', sharp=False, flat=True, instrument=instrument)
                    mock_note.assert_called_with(name, pitch='high', sharp=False, flat=True, instrument=instrument)

            # Test sharp notes
            sharp_note_names = ['A', 'C', 'D', 'F', 'G']
            for name in sharp_note_names:
                with self.subTest(name=name, pitch='low', sharp=True):
                    note(name, pitch='low', sharp=True, flat=False, instrument=instrument)
                    mock_note.assert_called_with(name, pitch='low', sharp=True, flat=False, instrument=instrument)
                
                with self.subTest(name=name, pitch='mid', sharp=True):
                    note(name, pitch='mid', sharp=True, flat=False, instrument=instrument)
                    mock_note.assert_called_with(name, pitch='mid', sharp=True, flat=False, instrument=instrument)
                
                with self.subTest(name=name, pitch='high', sharp=True):
                    note(name, pitch='high', sharp=True, flat=False, instrument=instrument)
                    mock_note.assert_called_with(name, pitch='high', sharp=True, flat=False, instrument=instrument)

    # def assert_notes_return_none(self, instrument, mock_sound):
    #     for name in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
    #         self.assertIsNone(note(name, pitch = 'low', instrument = instrument))
    #         self.assertIsNone(note(name, pitch = 'mid', instrument = instrument))
    #         self.assertIsNone(note(name, pitch = 'high', instrument = instrument))

    #     for name in ['A', 'B', 'D', 'E', 'G']:
    #         self.assertIsNone(note(name, pitch = 'low', sharp = False, flat = True, instrument = instrument))
    #         self.assertIsNone(note(name, pitch = 'mid', sharp = False, flat = True, instrument = instrument))
    #         self.assertIsNone(note(name, pitch = 'high', sharp = False, flat = True, instrument = instrument))

    #     for name in ['A', 'C', 'D', 'F', 'G']:
    #         self.assertIsNone(note(name, pitch = 'low', sharp = True, flat = False, instrument = instrument))
    #         self.assertIsNone(note(name, pitch = 'mid', sharp = True, flat = False, instrument = instrument))
    #         self.assertIsNone(note(name, pitch = 'high', sharp = True, flat = False, instrument = instrument))

if __name__ == '__main__':
    unittest.main()


