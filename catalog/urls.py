from django.urls import path
from . import views
from catalog.apps import CatalogConfig

app_name = CatalogConfig.name
print(app_name)

urlpatterns = [
    path("home/", views.show_home, name="home"),
    path("contacts/", views.show_contacts, name="contacts"),
]
