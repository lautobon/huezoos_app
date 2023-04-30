from django.shortcuts import render
from django.http import HttpResponse
from .forms import RegisterForm
from django.shortcuts import redirect

# Create your views here.

def home(request):
    return HttpResponse('joli')

def register_form(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})