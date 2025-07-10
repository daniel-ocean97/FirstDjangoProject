from django.urls import path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("home/", views.CatalogListView.as_view(), name="home"),
    path("contacts/", views.ContactsView.as_view(), name="contacts"),
    path(
        "product_detail/<int:pk>/",
        views.ProductDetailView.as_view(),
        name="product_detail",
    ),
    path("home/create", views.ProductCreateView.as_view(), name="product_create"),
    path(
        "home/update/<int:pk>", views.ProductUpdateView.as_view(), name="product_update"
    ),
    path(
        "home/delete/<int:pk>", views.ProductDeleteView.as_view(), name="product_delete"
    ),
    path("home/unpublish/<int:product_pk>", views.UnpublishProductView.as_view(), name="product_unpublish"),
]
