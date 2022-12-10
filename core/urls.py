"""PEA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import home, inscripcionTalleres,loginUsuario,registroUsuario,ingresarTaller, instructorNuevo, tallerIngresado1, tallerIngresado2 ,tallerIngresado3, crearnuevotaller, cuentausuario


urlpatterns = [
    path('', home,name="home"),
    path('inscripcionTalleres/', inscripcionTalleres,name="inscripcionTalleres"),
    path('loginUsuario/', loginUsuario,name="loginUsuario"),
    path('registroUsuario/', registroUsuario,name="registroUsuario"),
    path('ingresarTaller/', ingresarTaller,name="ingresarTaller"),
    path('instructorNuevo/', instructorNuevo,name="instructorNuevo"),
    path('tallerIngresado1/', tallerIngresado1 ,name="tallerIngresado1"),
    path('tallerIngresado2/', tallerIngresado2 ,name="tallerIngresado2"),
    path('tallerIngresado3/', tallerIngresado3 ,name="tallerIngresado3"),
    path('crearnuevotaller/', crearnuevotaller,name="crearnuevotaller"),
    path('cuentausuario/', cuentausuario ,name="cuentausuario"),
]


