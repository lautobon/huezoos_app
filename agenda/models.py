from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.

SERVICIOS = (
    ("Control", "Control"),
    ("Consulta", "Consulta"),
    ("Cirugía", "Cirugía"),
    ("Profilaxis", "Profilaxis"),
    ("Baño medicado", "Baño medicado"),
    ("Baño basico", "Baño basico"),
    ("Spa", "Spa"),
    ("Implante chip", "Implante chip"),
    ("Vacuna", "Vacuna")
)

HORARIOS = (
    ("8:00 AM", "8:00 AM"),
    ("9:00 AM", "9:00 AM"),
    ("10:00 AM", "10:00 AM")
)


class Species(models.Model):
    name = models.CharField(max_length=255)

    def get_races(self):
        return self.race_name.all()


class Race(models.Model):
    name = models.CharField(max_length=255)
    specie = models.ForeignKey(Species,
                               on_delete=models.CASCADE,
                               related_name='race_name')
    
class Huezoos_user(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_type = models.CharField(max_length=100)
    id_no = models.FloatField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    telephone1 = models.FloatField(max_length=255)
    telephone2 = models.FloatField(max_length=255, null=True, blank=True)


class Owner(models.Model):
    user = models.ForeignKey(Huezoos_user, 
                             on_delete=models.CASCADE,
                             related_name='owners')

    def get_pets(self):
        return self.pet_name.all()
    
class Manager(models.Model):
    staff = models.ForeignKey(Huezoos_user,
                              on_delete=models.CASCADE,
                              related_name='managers')


class Pet(models.Model):
    name = models.CharField(max_length=255)
    age = models.FloatField(max_length=30)
    birthday = models.DateField(default=datetime.now)
    owner = models.ForeignKey(Owner,
                              on_delete=models.CASCADE,
                              related_name='pet_name')
    race = models.ForeignKey(Race,
                             on_delete=models.CASCADE,
                             related_name='pet_race')
    
class Appointment(models.Model):
    user = models.ForeignKey(Owner,
                             on_delete=models.CASCADE)
    service = models.CharField(max_length=255, choices=SERVICIOS, default="Control")
    date_service = models.DateField(default=datetime.now)
    hour_service = models.CharField(max_length=255, choices=HORARIOS, default="8:00 AM")
