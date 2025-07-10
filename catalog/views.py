from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView, View)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from catalog.models import Product
from django.shortcuts import get_object_or_404, redirect

from .forms import ProductForm


class CatalogListView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"


class ContactsView(TemplateView):
    model = Product
    template_name = "contacts.html"


class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    context_object_name = "product"
    template_name = "catalog_form.html"
    success_url = reverse_lazy("catalog:home")

class UnpublishProductView(LoginRequiredMixin, View):
    def post(self, request, product_pk):
        product = get_object_or_404(Product, pk=product_pk)

        if not request.user.has_perm("can_unpublish_product"):
            raise PermissionDenied

        product.is_published = False
        product.save()

        return redirect("catalog:home")



class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    context_object_name = "product"
    template_name = "catalog_form.html"
    success_url = reverse_lazy("catalog:home")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalog_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")
