from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cotizar/', views.cotizar, name='cotizar'),
    path('equipo/', views.equipo, name='equipo'),
    path('trabaja-con-nosotros/', views.trabaja_con_nosotros, name='trabaja_con_nosotros'),
    path('login/', views.login, name='login'),
    path('sesion/', views.sesion, name='sesion'),
]
