from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("apps.pages.urls")),
    path("onboarding/", include("apps.onboarding.urls")),
    path("services/", include("apps.services.urls")),
    path("contact/", include("apps.contact.urls")),
    path("blog/", include("apps.blog.urls")),
    path("404/", TemplateView.as_view(template_name="404.html")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
