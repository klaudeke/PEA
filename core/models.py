from django.db import models

# Create your models here.

opcion_genero = [
    [0,"femenino"],
    [1,"masculino"],
    [2,"otro"]
]

class Instructor(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='nombre_instructor')
    email = models.EmailField()
    celular = models.CharField(max_length=12, verbose_name='fono_instructor')
    runInstructor = models.CharField(max_length=13, verbose_name='run_instructor')
    genero = models.IntegerField(choices=opcion_genero)
    certificado = models.CharField(max_length=100, verbose_name='certificado',null=True)
    #certificado = models.FileField(max_length=100, verbose_name='certificado',null=True)

    def __str__(self):
        return self.nombre
