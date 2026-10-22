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
            "company_name": "Doe Trucking LLC",
            "ein": "12-3456789",
            "mc_number": "MC-123456",
            "dot_number": "1234567",
            "phone": "(413) 555-1234",
            "email": "john@example.com",
            "fleet_type": "53' Dry Van",
            "cargo_insurance": "$100,000",
            "authority_active": True,
            "rate_lock_accepted": True,
            "rate_lock_months": 12,
        }
        response = self.client.post(reverse("carrier_onboarding"), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Carrier.objects.count(), 1)
