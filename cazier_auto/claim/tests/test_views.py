from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient


class ClaimsTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(email='kiki@kiki.com', username="kiki",
                                   password="cools3cretpass")

    def test_getting_claims(self):
        self.assertEqual(User.objects.count(), 1)

        user = User.objects.get(username='kiki')
        client = APIClient()
        client.force_authenticate(user=user)

        response = client.get('/api/claims.json', {})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
