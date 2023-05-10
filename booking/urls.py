from django.urls import path  
from .views import register_form, login_huezoos, auth_home, user_appointment

urlpatterns = [
    #path('', home, name='index'),
    path('', login_huezoos, name='login'),
    path('login', login_huezoos, name='redirect_login'),
    path('home', auth_home, name='home'),
    path('register', register_form, name='register'),
    path('appointment', user_appointment, name='appointment'),
    path('appointment/cancel', auth_home, name='appointment_cancel'),

]
