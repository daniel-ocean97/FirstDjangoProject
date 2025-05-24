from django.shortcuts import render
from catalog.models import Product


def show_home(request):
    products = Product.objects.all()
    context = {
        "products": products
    }
    return render(request, "home.html", context)


def show_contacts(request):
    return render(request, "contacts.html")


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        "product": product
    }
    return render(request, "product_detail.html", context)