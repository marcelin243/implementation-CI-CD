from django.test import TestCase
from django.test import SimpleTestCase
from user_app.tests import UtilisateurAPIViewTests  # Assurez-vous que le chemin est correct
import unittest

class CombinedTests(TestCase):
    def test_user_app_tests(self):
        # Créez une suite de tests et ajoutez-y les tests de UtilisateurAPIViewTests
        suite = unittest.TestSuite()
        suite.addTest(unittest.makeSuite(UtilisateurAPIViewTests))

        # Exécutez la suite de tests
        result = unittest.TextTestRunner().run(suite)

        # Vérifiez si tous les tests ont réussi
        self.assertTrue(result.wasSuccessful(), "Les tests  ont échoué.")