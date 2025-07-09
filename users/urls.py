from django.urls import path
from .views import RegisterView, CustomLoginView, CustomLogoutView

from catalog.apps import CatalogConfig

app_name = CatalogConfig.name


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]