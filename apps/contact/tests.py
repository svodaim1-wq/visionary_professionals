from django.test import TestCase, Client
from django.urls import reverse
from .models import ContactMessage

class ContactFormTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_form_get(self):
        response = self.client.get(reverse("contact"))
        self.assertEqual(response.status_code, 200)

    def test_form_post(self):
        data = {
            "name": "Jane Smith",
            "email": "jane@example.com",
            "phone": "555-5678",
            "message": "Interested in your services.",
        }
        response = self.client.post(reverse("contact"), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(ContactMessage.objects.count(), 1)
