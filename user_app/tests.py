from rest_framework import status
from rest_framework.test import APITestCase
from .models import utilisateur
from .serialisers import utilisateurSerializers

class UtilisateurAPIViewTests(APITestCase):
    def setUp(self):
        self.utilisateur1 = utilisateur.objects.create(nom='Alice', prenom='Alicia', adresse='alice@example.com')
        self.utilisateur2 = utilisateur.objects.create(nom='Bob', prenom='Bobby', adresse='bob@example.com')
        self.url = '/api/utilisateur/'  # Assurez-vous que cette URL est correcte

    def test_list_utilisateurs(self):
        response = self.client.get(self.url)
        utilisateurs = utilisateur.objects.all()
        serializer = utilisateurSerializers(utilisateurs, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_create_utilisateur(self):
        data = {'nom': 'Charlie', 'prenom': 'Charly', 'adresse': 'charlie@example.com'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(utilisateur.objects.count(), 3)  # Vérifie que 3 utilisateurs existent maintenant
        self.assertEqual(utilisateur.objects.get(id=response.data['id']).nom, 'Charlie')

    def test_update_utilisateur(self):
        data = {'nom': 'Alice Updated', 'prenom': 'Alicia Updated', 'adresse': 'alice.updated@example.com'}
        response = self.client.put(f'{self.url}{self.utilisateur1.id}/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.utilisateur1.refresh_from_db()
        self.assertEqual(self.utilisateur1.nom, 'Alice Updated')

    def test_delete_utilisateur(self):
        response = self.client.delete(f'{self.url}{self.utilisateur1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(utilisateur.objects.count(), 1)  # Vérifie que seul Bob reste