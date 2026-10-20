from django.urls import path
from . import views

urlpatterns = [
    path("", views.contact, name="contact"),
    path("specialist/", views.dispatch_specialist, name="dispatch_specialist"),
]
