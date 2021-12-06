from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from B_mainapp.forms import RegisterForm
from django.contrib.auth.models import User
from django.http import Http404, JsonResponse

# Create your views here.

def login_page(request):
    if request.user.is_authenticated:
        return redirect('estado-general')
    else:
        
        if request.method =='POST':

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('estado-general')
            else:
                messages.warning(request, 'Datos Incorrectos. Intente de nuevo.')
        
        
        return render(request, 'users/login.html',{
            'title':'Iniciar Sesión'
        })

def login_qr(request):
    if request.user.is_authenticated:
        return redirect('estado-general')

    else:
        qr=request.GET
        data = qr.__getitem__("qrdata")

        username, password= data.split('-')
        user = authenticate(request, username=username, password=password)
        login(request, user)
        
    
        return JsonResponse({'hola':'hola'})




@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def estado_general(request):
    return render(request, 'mainapp/estado-general.html',{
        'title': 'Estado General de Maquinas'
    })

@login_required(login_url='login')
def register_page(request):

    register_form=RegisterForm()

    if request.method == 'POST':
        register_form = RegisterForm(request.POST)

        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Te has registrado correctamente')
            return redirect('estado-general')

    return render(request, 'users/register.html',{
        'title': 'Registro',
        'register_form' : register_form
    })