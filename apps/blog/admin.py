from django.contrib import admin
from .models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ["title", "category", "author", "featured", "published_at"]
    list_filter = ["category", "featured"]
    search_fields = ["title", "content"]
    prepopulated_fields = {"slug": ("title",)}
