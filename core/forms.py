from django import forms
from .models import Instructor


class InstructorForm(forms.ModelForm):

    class Meta:
        model = Instructor
        #fields = ["nombre","email","celular","runInstructor","genero","certificado"]
        fields = '__all__'