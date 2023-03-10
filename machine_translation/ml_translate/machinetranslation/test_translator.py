import unittest
from translator import french_to_english, english_to_french

class TestTranslator(unittest.TestCase):
    def test_frenchToEnglish(self):
        # Test translation of 'Bonjour'
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        # Test null input
        self.assertEqual(french_to_english(None), None)
        
    def test_englishToFrench(self):
        # Test translation of 'Hello'
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        # Test null input
        self.assertEqual(english_to_french(None), None)
        
if __name__ == '__main__':
    unittest.main()
