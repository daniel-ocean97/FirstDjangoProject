from django.shortcuts import get_object_or_404

from .models import Category, Product


def get_products_by_category(id):
    """
    Возвращает товары для указанной категории
    """
    category = get_object_or_404(Category, pk=id)
    return Product.objects.filter(category=category, is_published=True)
