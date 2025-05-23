from django.shortcuts import render
from catalog.models import Product


def show_home(request):
    return render(request, "home.html")


def show_contacts(request):
    return render(request, "contacts.html")


def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {
        "product": product
    }
    return render(request, "product_detail.html", context)