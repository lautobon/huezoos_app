from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from .forms import RegisterForm
from django.utils import timezone, dateformat
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Appointment, Owner, Pet, Race
from .constants import SERVICIOS, HORARIOS, GENERO
# Create your views here.


@login_required
def auth_home(request):
    user = request.user
    if user.is_authenticated:
   
        owner:Owner = Owner.objects.get(email=user)
        user_id = owner.pk
        # Obtener todo y filtrar por 1 criterio
        pets: list[Pet] = Pet.objects.all().filter(owner_id=user_id)
        appointments: list[Appointment] = Appointment.objects.all().filter(user_id=user_id)

        if request.method == 'POST' and request.path == '/appointment/cancel':
            Appointment.objects.filter(id=request.POST["appointment_id"]).delete()

            return redirect('home')

        return render(request, 'home_user.html', {'user': owner, 'pets': pets, 'appointments': appointments})

    return render(request, 'login.html', {}) 


def login_huezoos(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        return redirect('login')

    else:
        return render(request, 'login.html', {})

def register_form(request):

    #print(GENERO.index(0))
    # races=Race.objects.all()
    # for race in races:
    #     for attr, value in race.__dict__.items():
    #         print(attr, value)

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():

            user = form.save()
            
            # pet = Pet(
            #     name='Rocky',
            #     age=3,
            #     birthday=dateformat.format(timezone.now(),  'Y-m-d'),
            #     gender='M',
            #     owner=user,
            #     race=Race.objects.get(pk=2)
            # )
            # pet.save()
            login(request, user)

            return redirect('home')
    else:

        form = RegisterForm()
 
    return render(request, 'register.html', {'form': form, 'errors': form.errors})

@login_required
def user_appointment(request):
    user=request.user


    if user.is_authenticated:
        owner:Owner = Owner.objects.get(email=user)
        # Obtener todo y filtrar por 1 criterio
        pets= Pet.objects.all().filter(owner_id=owner.pk)

        if request.method == 'POST':

            parsed_selected_date = datetime.strptime(request.POST['date_service'], '%Y-%m-%d')
            # Obtener 1 registro de la bd tabla pet
            selected_pet = Pet.objects.get(id=request.POST['selected_pet'])
           
            appointment= Appointment(
                service=request.POST['service'],
                hour_service='8:00 AM',
                date_service=dateformat.format(parsed_selected_date,  'Y-m-d'),
                user=owner,
                selected_pet=selected_pet,
                details=request.POST['details']
            )
            # Enviar info a bd
            appointment.save()
            
            # Enviar a usuario GET 
            return render(request, 'appointment_success.html')

        return render(request, 'appointment.html', {'services': SERVICIOS, 'pets': pets})
        
    else:
        return redirect('login')
    




