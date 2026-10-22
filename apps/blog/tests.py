from django.test import TestCase, Client
from django.urls import reverse
from .models import BlogPost

class BlogTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.post = BlogPost.objects.create(
            title="Top US Lanes 2026",
            category="industry-news",
            excerpt="Best routes this year.",
            content="Full content here.",
            featured=True,
        )

    def test_blog_list(self):
        response = self.client.get(reverse("blog_list"))
        self.assertEqual(response.status_code, 200)

    def test_blog_detail(self):
        response = self.client.get(reverse("blog_post", kwargs={"slug": self.post.slug}))
        self.assertEqual(response.status_code, 200)

    def test_slug_auto_generated(self):
        self.assertEqual(self.post.slug, "top-us-lanes-2026")
