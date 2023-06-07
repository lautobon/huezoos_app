from collections import defaultdict
from django.utils import timezone, dateformat
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
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

            for key, value in self.data.items():
                if key.startswith('pet'):
                    field_name = key.split('.')[2]
                    pet_num = int(key.split('.')[1]) - 1

                    pets[pet_num][field_name]=value
                
            pets = list(pets.values())

            for petEntry in pets:

                race = Race.objects.get(id=petEntry['razaMascota'])

                pet = Pet(
                    name=petEntry['nombreMascota'],
                    age=int(petEntry['edadMascota']),
                    gender=petEntry['generoMascota'],
                    owner=owner,
                    race=race
                )
                pet.save()

        return owner


class UserUpdateForm(UserChangeForm):
    class Meta:
        model = Owner
        fields = ( 'first_name', 'last_name', 'address', 'city', 'telephone1', 'telephone2')