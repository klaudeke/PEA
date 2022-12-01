from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request,'core/home.html')

def talleres(request):
    return render(request,'core/talleres.html')

def login(request):
    return render(request,'core/login.html')

def registro(request):
    return render(request,'core/registro.html')

def ingtalleres(request):
    return render(request,'core/ingtalleres.html')

def instructor(request):
    return render(request,'core/instructor.html')

def taller1(request):
    return render(request,'core/taller1.html')

def taller2(request):
    return render(request,'core/taller2.html')

def taller3(request):
    return render(request,'core/taller3.html')

def crearnuevotaller(request):
    return render(request,'core/crearnuevotaller.html')   
