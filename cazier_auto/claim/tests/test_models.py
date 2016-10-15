from django.test import TestCase
from cazier_auto.claim.models import Claim


class ClaimTestCase(TestCase):
    def setUp(self):
        Claim.objects.all()

    def test_all_claims(self):
        """Test claims"""
        claims = Claim.objects.all()
        self.assertEqual(list(claims), [])
