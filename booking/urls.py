from django.urls import path  
from .views import register_form, login_huezoos, auth_home, user_appointment, user_appointment_success, edit_user, logout_user

urlpatterns = [
    #path('', home, name='index'),
    path('', login_huezoos, name='login'),
    path('login', login_huezoos, name='redirect_login'),
    path('home', auth_home, name='home'),
    path('register', register_form, name='register'),

    path('appointment', user_appointment, name='appointment'),
    path('appointment/cancel', auth_home, name='appointment_cancel'),
    path('appointment/success', user_appointment_success, name='appointment_success'),


    path('pet/add', auth_home, name='add_pet'),
    path('pet/delete', auth_home, name='delete_pet'),

    path('user/edit', edit_user, name='edit_user'),

    path('user/logout', logout_user, name='logout_user')
    

]
