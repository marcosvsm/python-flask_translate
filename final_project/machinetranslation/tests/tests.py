import unittest

from translator import english_to_french, french_to_english

class TestTranslator(unittest.TestCase):
    def test_english_to_french(self):
            self.assertEqual(english_to_french('Hello'),'Bonjour')
    
    def test_none_english_to_french(self):
            message = 'None'
            self.assertIsNone(english_to_french(''),message)
    
    def test_french_to_english(self):
            self.assertEqual(french_to_english('Bonjour'),'Hello')

    def test_none_french_to_english(self):
            message= 'None'
            self.assertIsNone(french_to_english(''),message)

if __name__ == '__main__':
    unittest.main()
