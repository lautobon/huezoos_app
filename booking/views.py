from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

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

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():

            user = form.save()

            login(request, user)
            return redirect('home')
    else:

        form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'errors': form.errors})