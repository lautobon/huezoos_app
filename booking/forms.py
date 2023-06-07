from collections import defaultdict
from django.utils import timezone, dateformat
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .utils import save_user_pets
from .models import Owner, Pet, Race
from django import forms



class RegisterForm(UserCreationForm):

    class Meta:
        model = Owner
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name', 'id_type', 'id_no', 'address', 'city', 'telephone1', 'telephone2')

    
    def save(self, commit=True):
        owner = super().save(commit=False)
        pets = defaultdict(dict)

        # commit = guardar en bd
        if commit:
            owner.save()

            save_user_pets(self.data, owner)

        return owner


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = Owner
        fields = ( 'first_name', 'last_name', 'address', 'city', 'telephone1', 'telephone2')