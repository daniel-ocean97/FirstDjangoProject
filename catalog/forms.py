from django import forms
from django.core.exceptions import ValidationError

from .models import Product


class ProductForm(forms.ModelForm):

    FORBIDDEN_WORDS = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    class Meta:
        model = Product
        fields = ["name", "description", "image", "category", "price"]

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        self.fields["name"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Введите название продукта",
            }
        )

        self.fields["description"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
                "placeholder": "Введите название продукта",
            }
        )

        self.fields["image"].widget.attrs.update(
            {
                "class": "form-control",  # Добавление CSS-класса для стилизации поля
            }
        )

        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите стоимость продукта"}
        )

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price <= 0:
            raise ValidationError("Цена не может быть нулевой или отрицательной")

    def clean(self):
        cleaned_data = super().clean()
        self._validate_forbidden_words("name")
        self._validate_forbidden_words("description")
        return cleaned_data

    def _validate_forbidden_words(self, field_name):
        """Проверка наличия запрещённых слов в указанном поле"""
        value = self.cleaned_data.get(field_name)
        if not value:
            return
        value = value.lower()

        for forbidden_word in self.FORBIDDEN_WORDS:
            if forbidden_word in value:
                raise ValidationError(
                    "В названии или описании используется запрещённое слово"
                )
