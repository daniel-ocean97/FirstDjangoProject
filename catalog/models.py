from django.db import models
from config.settings import AUTH_USER_MODEL


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(
        verbose_name="Фото товара", null=True, blank=True, upload_to="product_photo/"
    )
    category = models.ForeignKey(
        verbose_name="Категория",
        to="Category",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    price = models.PositiveIntegerField(verbose_name="Цена")
    created_at = models.DateField(verbose_name="Создано", auto_now_add=True)
    updated_at = models.DateField(verbose_name="Последний раз обновлено", auto_now=True)
    is_published = models.BooleanField(default=False, verbose_name="Опубликован")
    owner = models.ForeignKey(
        AUTH_USER_MODEL,  # Используем кастомную модель пользователя
        on_delete=models.SET_NULL,  # При удалении пользователя продукт остаётся
        null=True,
        blank=True,
        verbose_name="Владелец",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ("category", "price")

        permissions = [("can_unpublish_product", "Can unpublish product"),
                       ]

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    created_at = models.DateField(verbose_name="Создано", auto_now_add=True)
    updated_at = models.DateField(verbose_name="Последний раз обновлено", auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
