from django.core.management import BaseCommand

from users.models import CatalogUser

class Command(BaseCommand):
    def handle(self, *args, **options):
        user = CatalogUser.objects.create(email="admin@admin.ru")
        user.set_password("123qwe")
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save()

