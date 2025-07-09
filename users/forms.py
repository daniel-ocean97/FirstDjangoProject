from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import CatalogUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CatalogUser
        fields = ["email",]


class CustomAuthenticationForm(AuthenticationForm):
    pass