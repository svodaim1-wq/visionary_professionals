from django.urls import path
from . import views

urlpatterns = [
    path("carrier/", views.carrier_onboarding, name="carrier_onboarding"),
    path("pod/", views.pod_submission, name="pod_submission"),
]
