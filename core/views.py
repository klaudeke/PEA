from django.shortcuts import render, redirect, get_list_or_404
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import InstructorForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import *
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

def agregar_instructor(request):

    data ={
         
    }

    return render(request, 'core/instructorCRUD/agregar.html')

#CRUD - INSTRUCTOR
#AGREGAR
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

    return render(request,'core/instructorCRUD/instructorNuevo.html', data)

#LISTAR
def listar_instructor(request):
    instructor = Instructor.objects.all()

    data = {
        'instructor': instructor
    }
    return render(request, 'core/instructorCRUD/listarInstructor.html',data)

#MODIFICAR
def modificar_instructor(request, id):

    id_instructor = Instructor.objects.get(id=id)

    data = {
        'form': InstructorForm(instance=id_instructor)
    }

    if request.method=='POST':
        formulario= InstructorForm(data=request.POST,instance=id_instructor)
        if formulario.is_valid:
            formulario.save()
            return redirect(to="listar_instructor")
        data["form"] = formulario

    return render(request, 'core/instructorCRUD/modificarInstructor.html',data)

#ELIMINAR
def eliminar_instructor(request, id):
    id_instructor = Instructor.objects.get(id=id)
  
    id_instructor.delete()

    return redirect(to="listar_instructor")