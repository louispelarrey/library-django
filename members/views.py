from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.db import IntegrityError

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('board:board')
        else:
            messages.error(request, 'Le nom de compte ou le mot de passe est incorrect')
    context = {}
    return render(request, 'authenticate/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('members:login')

def register_user(request):
    try :
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']
            user = User.objects.create_user(username, email, password)
            user.save()
            return redirect('members:login')
    except IntegrityError:
        messages.error(request, 'Le nom de compte existe déjà')
    except :
        messages.error(request, 'Une erreur est survenue')
    context = {}
    return render(request, 'authenticate/register.html', context)