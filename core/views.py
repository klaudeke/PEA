from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'core/home.html')

def inscripcionTalleres(request):
    return render(request,'core/inscripcionTalleres.html')

def login(request):
    return render(request,'core/login.html')

def registro(request):
    return render(request,'core/registro.html')

def ingresarTaller(request):
    return render(request,'core/ingresarTaller.html')

def instructorNuevo(request):
    return render(request,'core/instructorNuevo.html')

def taller1(request):
    return render(request,'core/taller1.html')

def taller2(request):
    return render(request,'core/taller2.html')

def taller3(request):
    return render(request,'core/taller3.html')

def crearnuevotaller(request):
    return render(request,'core/crearnuevotaller.html')   

def cuentausuario(request):
    return render(request,'core/cuentausuario.html')   

