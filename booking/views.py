from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm
from django.shortcuts import redirect
from django.contrib.auth import login

# Create your views here.

def home(request):
    return HttpResponse('joli')

def register_form(request):

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form.is_valid)
        if form.is_valid():

            user = form.save()
            print(user)
            login(request, user)
            return redirect('index')
    else:

        form = RegisterForm()
    return render(request, 'register.html', {'form': form, 'errors': form.errors})