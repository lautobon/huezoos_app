from django.urls import path  
from .views import home, register_form, login_huezoos, auth_home

urlpatterns = [
    path('', home, name='index'),
    path('home', auth_home, name='home'),
    path('register', register_form, name='register'),
    path('login', login_huezoos, name='login')
]
