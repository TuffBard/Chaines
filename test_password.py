# coding: utf-8 
import unittest
import password as pwd

class TestPassword(unittest.TestCase):

    def test_getNextNormal(self):
        self.assertEqual(pwd.getNext("aaaaa"), "aaaab")

    def test_getNextEndLine(self):
        self.assertEqual(pwd.getNext("aaaaz"), "aaaba")

    def test_getNextEndPwd(self):
        self.assertEqual(pwd.getNext("zzzzz"), "aaaaa")

    def test_hasSeriesTrue(self):
        self.assertEqual(pwd.hasSeries("abcde"), True)

    def test_hasSeriesFalse(self):
        self.assertEqual(pwd.hasSeries("abacc"), False)

    def test_hasTwoPairsTrue(self):
        self.assertEqual(pwd.hasTwoPairs("baacc"), True)

    def test_hasTwoPairsFalse(self):
        self.assertEqual(pwd.hasTwoPairs("abacc"), False)

    def test_hasNoBadCharTrue(self):
        self.assertEqual(pwd.hasNoBadChar("baacc"), True)

    def test_hasNoBadCharFalse(self):
        self.assertEqual(pwd.hasNoBadChar("&é(-è_ççà)="), False)

    


# Permet d'exécuter les tests si ce fichier est exécuté
unittest.main()
