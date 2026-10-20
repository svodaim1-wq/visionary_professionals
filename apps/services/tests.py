from django.test import TestCase, Client
from django.urls import reverse
import json

class ServicesTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_services_page(self):
        response = self.client.get(reverse("services_list"))
        self.assertEqual(response.status_code, 200)

    def test_api_corridor_rate_valid(self):
        response = self.client.get(reverse("api_corridor_rate"), {
            "origin": "jhb",
            "destination": "durban",
            "vehicle": "superlink",
            "distance": "600"
        })
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertIn("total_estimate", data)

    def test_api_corridor_rate_missing_params(self):
        response = self.client.get(reverse("api_corridor_rate"))
        self.assertEqual(response.status_code, 400)

    def test_api_corridor_rate_invalid_corridor(self):
        response = self.client.get(reverse("api_corridor_rate"), {
            "origin": "jhb",
            "destination": "unknown",
            "vehicle": "superlink",
            "distance": "100"
        })
        self.assertEqual(response.status_code, 404)
