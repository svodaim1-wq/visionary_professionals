from django.shortcuts import render, get_object_or_404
from .models import BlogPost

def blog_list(request):
    category = request.GET.get("category", "")
    posts = BlogPost.objects.all()
    if category:
        posts = posts.filter(category=category)
    featured = posts.filter(featured=True).first()
    context = {
        "posts": posts,
        "featured": featured,
        "current_category": category,
        "categories": BlogPost.CATEGORY_CHOICES,
    }
    return render(request, "blog/list.html", context)

def blog_post(request, slug):
    post = get_object_or_404(BlogPost, slug=slug)
    related = BlogPost.objects.filter(category=post.category).exclude(pk=post.pk)[:3]
    return render(request, "blog/detail.html", {"post": post, "related": related})
