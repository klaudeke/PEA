from django import forms
from .models import Instructor
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class InstructorForm(forms.ModelForm):
    
    # nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # celular = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # runInstructor = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # genero = forms.IntegerField(widget=forms.CheckboxInput(attrs={"class":"dropdown-menu"}))
    # AQUI ESTA EL PROBLEMA EN LA CARGA DE CERTIFICADO
    # certificado = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Instructor
        #fields = ["nombre","email","celular","runInstructor","genero","certificado"]
        fields = '__all__'


class CustomUserCreationForm(UserCreationForm):
        
        class Meta:
            model = User
            fields = ['username','email','telefono','password1','password2']