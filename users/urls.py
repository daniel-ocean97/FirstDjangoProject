from django.urls import path

from catalog.apps import CatalogConfig

from .views import CustomLoginView, CustomLogoutView, RegisterView

app_name = CatalogConfig.name


urlpatterns = [
    path("login/", CustomLoginView.as_view(), name="login"),
    path("logout/", CustomLogoutView.as_view(), name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
]
