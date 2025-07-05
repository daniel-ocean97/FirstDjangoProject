from catalog.models import Product
from django.views.generic import ListView, TemplateView, DetailView

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
