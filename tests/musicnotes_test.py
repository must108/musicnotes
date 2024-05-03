import unittest
from musicnotes import note

class testnotes(unittest.TestCase):
    def test_piano_notes(self):
        for name in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
            self.assertIsNone(note(name, pitch = 'low', instrument = 'piano'))
            self.assertIsNone(note(name, pitch = 'mid', instrument = 'piano'))
            self.assertIsNone(note(name, pitch = 'high', instrument = 'piano'))

        for name in ['A', 'B', 'D', 'E', 'G']:
            self.assertIsNone(note(name, pitch = 'low', sharp = False, flat = True, instrument = 'piano'))
            self.assertIsNone(note(name, pitch = 'mid', sharp = False, flat = True, instrument = 'piano'))
            self.assertIsNone(note(name, pitch = 'high', sharp = False, flat = True, instrument = 'piano'))

        for name in ['A', 'C', 'D', 'F', 'G']:
            self.assertIsNone(note(name, pitch = 'low', sharp = True, flat = False, instrument = 'piano'))
            self.assertIsNone(note(name, pitch = 'mid', sharp = True, flat = False, instrument = 'piano'))
            self.assertIsNone(note(name, pitch = 'high', sharp = True, flat = False, instrument = 'piano'))

    def test_guitar_notes(self):
        for name in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
            self.assertIsNone(note(name, pitch = 'low', instrument = 'guitar'))
            self.assertIsNone(note(name, pitch = 'mid', instrument = 'guitar'))
            self.assertIsNone(note(name, pitch = 'high', instrument = 'guitar'))

        for name in ['A', 'B', 'D', 'E', 'G']:
            self.assertIsNone(note(name, pitch = 'low', sharp = False, flat = True, instrument = 'guitar'))
            self.assertIsNone(note(name, pitch = 'mid', sharp = False, flat = True, instrument = 'guitar'))
            self.assertIsNone(note(name, pitch = 'high', sharp = False, flat = True, instrument = 'guitar'))

        for name in ['A', 'C', 'D', 'F', 'G']:
            self.assertIsNone(note(name, pitch = 'low', sharp = True, flat = False, instrument = 'guitar'))
            self.assertIsNone(note(name, pitch = 'mid', sharp = True, flat = False, instrument = 'guitar'))
            self.assertIsNone(note(name, pitch = 'high', sharp = True, flat = False, instrument = 'guitar'))

if __name__ == '__main__':
    unittest.main()


