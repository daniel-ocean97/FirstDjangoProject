from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin,
                                        UserPassesTestMixin)
from django.core.cache import cache
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  TemplateView, UpdateView, View)

from catalog.models import Category, Product

from .forms import ProductForm
from .services import get_products_by_category


class CatalogListView(ListView):
    model = Product
    template_name = "home.html"
    context_object_name = "products"

    def get_queryset(self):
        queryset = cache.get("my_queryset")
        if not queryset:
            queryset = super().get_queryset()
            cache.set("my_queryset", queryset, 60 * 15)  # Кешируем данные на 15 минут
        return queryset


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

    def form_valid(self, form):
        # Устанавливаем текущего пользователя как владельца
        form.instance.owner = self.request.user
        return super().form_valid(form)


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

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().owner != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class ProductDeleteView(PermissionRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = "catalog_confirm_delete.html"
    success_url = reverse_lazy("catalog:home")
    permission_required = "catalog.delete_product"

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().owner != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def test_func(self):
        return self.request.user.groups.filter(name="Moderators").exists()


def category_products_view(request, category_id):
    """Отображает товары по ID категории"""
    try:
        products = get_products_by_category(category_id)
    except Category.DoesNotExist:
        return render(request, "404.html", status=404)

    category = get_object_or_404(Category, id=category_id)

    return render(
        request,
        "category_products.html",
        {
            "products": products,
            "category": category,
            "all_categories": Category.objects.all(),
        },
    )
