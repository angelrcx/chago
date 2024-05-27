
# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from sqlite3 import IntegrityError

def home(request):
    return render(request, 'registration/home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'registration/login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = AuthenticationForm()
        return render(request, 'registration/login.html', {'form': form})

def signup_view(request):
    # lógica para el signup
    if request.method == 'GET':
        return render(request, 'registration/signup.html',{
        'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user =User.objects.create_user(username=request.POST['username'],password=request.POST['password1'] )
                user.save()
                login(request,user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signup.html'), {
                    'form': UserCreationForm,
                    "error": 'User already exist'
                }
        return render(request,'signup.html'), {
            'form': UserCreationForm,
            "error": 'Password do not match'
        }
    
def logout_view(request):
    logout(request)
    return redirect('home')

