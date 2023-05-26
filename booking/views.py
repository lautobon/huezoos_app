from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
from .forms import RegisterForm
from django.utils import timezone, dateformat
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Appointment, Owner, Pet, Race, Species
from .constants import SERVICIOS, HORARIOS, GENERO
# Create your views here.


@login_required
def auth_home(request):
    user = request.user
    if user.is_authenticated:
   
        owner: Owner = Owner.objects.get(email=user)
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

    races = Race.objects.all()
    species = Species.objects.all()

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():

            user = form.save()
            
            
            login(request, user)

            return redirect('home')
    else:

        form = RegisterForm()
 
    return render(request, 'register.html', {'form': form, 'errors': form.errors, 'races': races, 'species': species})

@login_required
def user_appointment(request):
    user=request.user

    context_edit = {}

    if user.is_authenticated:
        owner:Owner = Owner.objects.get(email=user)
        # Obtener todo y filtrar por 1 criterio
        pets= Pet.objects.all().filter(owner_id=owner.pk)

        appointment_id = request.GET.get('id')

        if appointment_id:
            #appointment_edit = Appointment.objects.filter(user_id=owner.pk).filter(id=appointment_id)
            appointment_edit = Appointment.objects.get(id=appointment_id)
       
            context_edit = appointment_edit

            #return render(request, 'appointment.html', {'services': SERVICIOS, 'pets': pets})

        if request.method == 'POST':

            appointment_id = request.POST['appointment_id']

            print(request.POST['date_service'])
            parsed_selected_date = datetime.strptime(request.POST['date_service'], '%Y-%m-%d')
            # Obtener 1 registro de la bd tabla pet
            selected_pet = Pet.objects.get(id=request.POST['selected_pet'])

            if appointment_id:
                db_appointment = Appointment.objects.get(id=appointment_id)

                db_appointment.service =request.POST['service']
                db_appointment.date_service =dateformat.format(parsed_selected_date,  'Y-m-d')
                db_appointment.selected_pet =selected_pet
                db_appointment.details =request.POST['details']

                db_appointment.save(force_update=True, update_fields=['service', 'date_service', 'selected_pet', 'details'])
                return redirect('home')

            else:   
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
                
                request.session['appointment'] = {
                    'pet_name': selected_pet.name,
                    'date_service': appointment.date_service,
                    'hour_service': appointment.hour_service,
                    'service': appointment.service
                }

                # Enviar a usuario GET 
                return redirect('appointment_success')

        return render(request, 'appointment.html', {'services': SERVICIOS, 'pets': pets, 'edit': context_edit})
        
    else:
        return redirect('login')
    

def user_appointment_success(request):
    context = request.session.get('appointment')
    print(context)
    if context is None:
        return redirect('appointment')
    return render(request, 'appointment_success.html', context)
