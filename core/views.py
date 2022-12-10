from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'core/home.html')

def inscripcionTalleres(request):
    return render(request,'core/inscripcionTalleres.html')

def loginUsuario(request):
    return render(request,'core/loginUsuario.html')

def registroUsuario(request):
    return render(request,'core/registroUsuario.html')

def ingresarTaller(request):
    return render(request,'core/ingresarTaller.html')

def instructorNuevo(request):
    return render(request,'core/instructorNuevo.html')

def tallerIngresado1(request):
    return render(request,'core/tallerIngresado1.html')

def tallerIngresado2(request):
    return render(request,'core/tallerIngresado2.html')

def tallerIngresado3(request):
    return render(request,'core/tallerIngresado3.html')

def crearnuevotaller(request):
    return render(request,'core/crearnuevotaller.html')   

def cuentausuario(request):
    return render(request,'core/cuentausuario.html')   

