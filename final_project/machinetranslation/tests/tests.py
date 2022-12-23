import unittest
from translator import french_to_english, english_to_french
class TestFrenchToEnglish(unittest.TestCase):
    def test_null(self):
        self.assertNotEqual(french_to_english('None'), '   ')  
    
    def test_hello(self): 
        self.assertEqual(french_to_english("Bonjour"),"Hello")
    


class TestEnglishToFrench(unittest.TestCase) :
    def test_null(self): 
        self.assertNotEqual(english_to_french('None'), '   ')  
    
    def test_bonjour(self): 
        self.assertEqual(english_to_french("Hello"), "Bonjour")
    
if __name__ == '__main__':
    unittest.main()

