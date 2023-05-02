from django.contrib.auth.forms import UserCreationForm
from .models import Owner

class RegisterForm(UserCreationForm):
    
    class Meta:
        model = Owner
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'id_type', 'id_no', 'address', 'city', 'telephone1', 'telephone2')
