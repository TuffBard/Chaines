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


# Permet d'exécuter les tests si ce fichier est exécuté
unittest.main()
