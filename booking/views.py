from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm
from django.utils import timezone, dateformat
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import Appointment, Owner, Pet, Race
from .constants import SERVICIOS, HORARIOS, GENERO
# Create your views here.


def home(request):
    return HttpResponse('joli')

@login_required
def auth_home(request):
    user = request.user
    context = {}
    if user.is_authenticated:
        context['msn'] = 'Autenticado'

    return render(request, 'index.html', context)

def login_huezoos(request):
    if request.method == 'POST':
        email = request.POST["email"]
        password = request.POST["password"]

        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        
        return redirect('index')

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
    user= request.user
    owner= Owner.objects.get(email=user)
    if user.is_authenticated:

        return render(request, 'appointment.html', {'services': SERVICIOS})
        # appointment= Appointment(service='Control', hour_service='8:00 AM', date_service=dateformat.format(timezone.now(),  'Y-m-d'), user=owner)
        # appointment.save()
    else:
        return redirect('login')


