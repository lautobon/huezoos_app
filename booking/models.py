from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager, BaseUserManager
from django.utils import timezone
from django.conf import settings
from datetime import date, datetime, time
from .constants import SERVICIOS, HORARIOS, GENERO, TIPOS_ID

# Create your models here.


class Species(models.Model):
    name = models.CharField(max_length=255)

    def get_races(self):
        return self.race_name.all()


class Race(models.Model):
    name = models.CharField(max_length=255)
    specie = models.ForeignKey(Species,
                               on_delete=models.CASCADE,
                               related_name='race_name')


class BaseHuezoosUserManager(BaseUserManager):
    def create_user(self, email, password=None, is_admin=False, is_staff=False, is_active=True, is_superuser=False):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        user = self.model(
            email=self.normalize_email(email)
        )
        #user.full_name = full_name
        user.set_password(password)  # change password to hash
        # user.profile_picture = profile_picture
        user.admin = is_admin
        user.staff = is_staff
        user.superuser = is_superuser
        user.active = is_active
        user.save(using=self._db)
        return user
        
    def create_superuser(self, email, password=None, is_admin=True, is_staff=True, **extra_fields):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")

        # user = self.model(
        #     email=self.normalize_email(email)
        # )
        # user.full_name = full_name
        # user.set_password(password)
        # user.profile_picture = profile_picture
        # user.admin = True
        # user.staff = True
        # user.active = True
        # user.save(using=self._db)
        return self.create_user(email, password, is_admin=True, is_staff=True, is_superuser=True)

class HuezoosUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    id_type = models.CharField(max_length=100, choices=TIPOS_ID, default="CC")
    id_no = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    telephone1 = models.CharField(max_length=255)
    telephone2 = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'id_type', 'id_no', 'address', 'telephone1']

    objects = BaseHuezoosUserManager()

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

class Owner(HuezoosUser):
    role = models.CharField(max_length=255, default='responsable')
    
    def get_pets(self):
        return self.objects.get()


class HuezoosManager(HuezoosUser):
    role = models.CharField(max_length=255, default='gestor')

    
class Pet(models.Model):
    name = models.CharField(max_length=255)
    age = models.SmallIntegerField()
    birthday = models.DateField(default=timezone.now)
    owner = models.ForeignKey(Owner,
                              on_delete=models.CASCADE,
                              related_name='pet_name')
    race = models.ForeignKey(Race,
                             on_delete=models.CASCADE,
                             related_name='pet_race')
    gender = models.CharField(max_length=255, choices=GENERO)
    
class Appointment(models.Model):
    user = models.ForeignKey(Owner,
                             on_delete=models.CASCADE)
    selected_pet = models.ForeignKey(Pet,on_delete=models.CASCADE)
    service = models.CharField(max_length=255, choices=SERVICIOS, default="Control")
    date_service = models.DateField(default=timezone.now)
    hour_service = models.CharField(max_length=255, choices=HORARIOS, default="8:00 AM")
    details = models.CharField(max_length=255, null=True, blank=True)
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"