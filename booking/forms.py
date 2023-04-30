from django.contrib.auth.forms import UserCreationForm
from .models import Owner

class RegisterForm(UserCreationForm):
    class Meta:
        model = Owner
        fields = ('username', 'email', 'password1', 'password2')