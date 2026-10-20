from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("equipment/", views.equipment, name="equipment"),
    path("pricing/", views.pricing, name="pricing"),
    path("solutions/", views.solutions, name="solutions"),
    path("portal/", views.portal, name="portal"),
    path("portal/dashboard/", views.dashboard, name="dashboard"),
    path("portal/settings/", views.settings_page, name="settings_page"),
    path("portal/login/", views.carrier_login, name="carrier_login"),
    path("portal/logout/", views.carrier_logout, name="carrier_logout"),
    path("carrier-packet/", views.carrier_packet, name="carrier_packet"),
    path("schedule-call/", views.schedule_call, name="schedule_call"),
    path("help/", views.help_page, name="help"),
    path("search/", views.search, name="search"),
]
