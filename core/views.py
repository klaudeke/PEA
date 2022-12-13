from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import InstructorForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.


def home(request):
    return render(request,'core/home.html')

def inscripcionTalleres(request):
    return render(request,'core/inscripcionTalleres.html')

def loginUsuario(request):
    return render(request,'core/loginUsuario.html')

def registroUsuario(request):
    data = {
        'form' : CustomUserCreationForm
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username = formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "registro exitoso")
            return redirect(to="home")
        data["form"] = formulario
    return render(request,'registration/registro.html', data)

def ingresarTaller(request):
    return render(request,'core/ingresarTaller.html')

def instructorNuevo(request):
    data = {
        'form':InstructorForm()
    }
    if request.method == 'POST':
        formulario = InstructorForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "formulario enviado"
        else:
            data["form"] = formulario

    return render(request,'core/instructorNuevo.html', data)

def tallerIngresado1(request):
    return render(request,'core/tallerIngresado1.html')

def tallerIngresado2(request):
    return render(request,'core/tallerIngresado2.html')

def tallerIngresado3(request):
    return render(request,'core/tallerIngresado3.html')

def crearNuevoTaller(request):
    return render(request,'core/crearNuevoTaller.html')   

def cuentausuario(request):
    return render(request,'core/cuentausuario.html')   

