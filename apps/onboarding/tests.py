from django.test import TestCase, Client
from django.urls import reverse
from .models import Carrier

class CarrierOnboardingTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_form_get(self):
        response = self.client.get(reverse("carrier_onboarding"))
        self.assertEqual(response.status_code, 200)

    def test_form_post(self):
        data = {
            "full_legal_name": "John Doe",
            "id_number": "9001015001089",
            "company_name": "Doe Trucking LLC",
            "cipc_registration": "2023/123456/07",
            "mc_number": "MC-123456",
            "phone": "555-1234",
            "email": "john@example.com",
            "fleet_type": "Superlink (34T)",
            "git_insurance": "R500,000",
            "has_prdp": True,
            "rate_lock_accepted": True,
            "rate_lock_months": 12,
        }
        response = self.client.post(reverse("carrier_onboarding"), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Carrier.objects.count(), 1)
