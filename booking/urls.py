from django.urls import path  
from .views import home, register_form

urlpatterns = [
    path('', home, name='index'),
    path('register', register_form, name='register')
]
