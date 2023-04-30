from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.conf import settings

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
    
# class Huezoos_user(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     id_type = models.CharField(max_length=100)
#     id_no = models.FloatField(max_length=255)
#     address = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     telephone1 = models.FloatField(max_length=255)
#     telephone2 = models.FloatField(max_length=255, null=True, blank=True)


#class Owner(AbstractUser):
    # user = models.OneToOneField(User, 
    #                          on_delete=models.CASCADE,
    #                          related_name='owners')
    # id_type = models.CharField(max_length=100, null=True, blank=True)
    # id_no = models.FloatField(max_length=255, null=True, blank=True)
    # address = models.CharField(max_length=255, null=True, blank=True)
    # city = models.CharField(max_length=255, null=True, blank=True)
    # telephone1 = models.FloatField(max_length=255, null=True, blank=True)
    # telephone2 = models.FloatField(max_length=255, null=True, blank=True)

    # def get_pets(self):
    #     return self.pet_name.all()

class Owner(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

# class Manager(models.Model):
#     staff = models.ForeignKey(Huezoos_user,
#                               on_delete=models.CASCADE,
#                               related_name='managers')

class Pet(models.Model):
    name = models.CharField(max_length=255)
    age = models.FloatField(max_length=30)
    birthday = models.DateField(default=timezone.now)
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
    date_service = models.DateField(default=timezone.now)
    hour_service = models.CharField(max_length=255, choices=HORARIOS, default="8:00 AM")
