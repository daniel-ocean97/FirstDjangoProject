from django.db import models


# Create your models here.
class Post(models.Model):
    header = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(
        verbose_name="Изображение", null=True, blank=True, upload_to="blog_photo/"
    )
    created_at = models.DateField(verbose_name="Создано", auto_now_add=True)
    publication_attribute = models.BooleanField(default=True)
    views_counter = models.PositiveIntegerField(
        verbose_name="Счётчик просмотров", default=0
    )

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ("header", "content")
