from django.urls import path
from . import views

app_name = "catalog"

urlpatterns = [
    path("home/", views.show_home, name="home"),
    path("contacts/", views.show_contacts, name="contacts")
]