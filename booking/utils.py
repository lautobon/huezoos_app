from collections import defaultdict
from typing import Any, Dict

from booking.models import Owner, Pet, Race

def save_user_pets(request_data: Dict[str, Any], owner: Owner):
    pets = defaultdict(dict)

    for key, value in request_data.items():
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

