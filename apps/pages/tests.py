from django.test import TestCase, Client

class PagesTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_equipment_page(self):
        response = self.client.get("/equipment/")
        self.assertEqual(response.status_code, 200)

    def test_pricing_page(self):
        response = self.client.get("/pricing/")
        self.assertEqual(response.status_code, 200)
