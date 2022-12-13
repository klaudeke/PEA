from django import forms
from .models import Instructor


class InstructorForm(forms.ModelForm):

    # nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # email = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # celular = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # runInstructor = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    # genero = forms.IntegerField(widget=forms.CheckboxInput(attrs={"class":"dropdown-menu"}))
    # certificado = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    class Meta:
        model = Instructor
        #fields = ["nombre","email","celular","runInstructor","genero","certificado"]
        fields = '__all__'