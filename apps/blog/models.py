from django.db import models
from django.urls import reverse
from django.utils.text import slugify

class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ("industry-news", "Industry News"),
        ("dispatch-tips", "Dispatch Tips"),
        ("compliance", "Compliance"),
        ("new-carriers", "New Carriers"),
        ("route-planning", "Route Planning"),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="industry-news")
    excerpt = models.TextField()
    content = models.TextField()
    author = models.CharField(max_length=100, default="Visionary Team")
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    featured = models.BooleanField(default=False)
    reading_time = models.PositiveIntegerField(default=5)
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-published_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_post", kwargs={"slug": self.slug})
