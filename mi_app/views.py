from django.shortcuts import render
from .models import postulacion

# Create your views here.

def index(request):
    postulaciones=postulacion.objects.all()
    context={"postulaciones":postulaciones}
    return render(request, 'mi_app/index.html',context)
def crud(request):
    postulaciones=postulacion.objects.all()
    context={"postulaciones":postulaciones}
    return render(request, 'mi_app/crud.html',context)
def home(request):
    return render(request, 'mi_app/principal.html')
def cotizar(request):
    return render(request, 'mi_app/cotizar.html')
def equipo(request):
    return render(request, 'mi_app/qs.html')
def trabaja_con_nosotros(request):
    return render(request, 'mi_app/tcn.html')
def login(request):
    return render(request, 'mi_app/login.html')
def sesion(request):
    return render(request, 'mi_app/sesion.html')

def addPostulante(request):
    if request.method is not "POST":
        return render(request, 'mi_app/addPostulante.html')
def delPostulante(request,pk):
    context={}
    try:
        postulante=postulacion.objects.get(nombre_post=pk)

        postulante.delete()
        mensaje="postulante eliminado con exito."
        postulantes=postulante.objects.all()
        context = {'postulantes':postulantes, 'mensaje':mensaje}
        return render(request,'mi_app/crud.html',context)
    except:
        mensaje="postulante no encontrado"
        postulantes=postulante.objects.all()
        context = {'postulantes':postulantes, 'mensaje':mensaje}
        return render(request,'mi_app/crud.html',context)

def modPostulante(request,pk):
    if pk != "":
        postulante=postulacion.objects.get(nombre_post=pk)
        context={'postulante':postulante}
        if postulante:
            return render(request,'mi_app/modPostulante.html',context)
        else:
            context={'mensaje':"Error, postulante no encontrado"}
            return render(request,'mi_app/crud.html',context)