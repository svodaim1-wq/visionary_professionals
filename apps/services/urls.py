from django.urls import path
from . import views

urlpatterns = [
    path("", views.services_list, name="services_list"),
    path("api/corridor-rate/", views.api_corridor_rate, name="api_corridor_rate"),
]
