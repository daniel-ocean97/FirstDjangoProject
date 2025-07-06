from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView)

from catalog.models import Product

from .forms import ProductForm


class CatalogListView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"


class ContactsView(TemplateView):
    model = Product
    template_name = "contacts.html"


class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    context_object_name = "product"
    template_name = "catalog_form.html"
    success_url = reverse_lazy("catalog:home")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    context_object_name = "product"
    template_name = "catalog_form.html"
    success_url = reverse_lazy("catalog:home")


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalog_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")
