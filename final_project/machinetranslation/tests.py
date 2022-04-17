import unittest
from translator import english_to_french, french_to_english
 
class Test_english_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french(None),"Please enter some text")#Vefifica vacios
    def test2(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")#Comprueba OK
 
class Test_french_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english(None),"Veuillez saisir du texte")#Vefifica vacios
    def test2(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")#Comprueba OK
 
unittest.main()