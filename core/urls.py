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
from .views import home, talleres,login,registro,ingtalleres, instructor, taller1, taller2,taller3 


urlpatterns = [
    path('', home,name="home"),
    path('talleres/', talleres,name="talleres"),
    path('login/', login,name="login"),
    path('registro/', registro,name="registro"),
    path('ingtalleres/', ingtalleres,name="ingtalleres"),
    path('instructor/', instructor,name="instructor"),
    path('taller1/', taller1 ,name="taller1"),
    path('taller2/', taller2 ,name="taller2"),
    path('taller3/', taller3 ,name="taller3"),
]


