from django.core.management.base import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):
    help = "Delete data"

    def handle(self, *args, **options):
        # Удаляем существующие записи
        Product.objects.all().delete()
        Category.objects.all().delete()
