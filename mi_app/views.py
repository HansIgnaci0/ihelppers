from django.shortcuts import render, redirect
from .models import postulacion
from .models import lenguaje

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
    lenguajes=lenguaje.objects.all()
    context={"lenguajes":lenguajes}
    return render(request, 'mi_app/tcn.html', context)
def login(request):
    return render(request, 'mi_app/login.html')
def sesion(request):
    return render(request, 'mi_app/sesion.html')

def addPostulante(request):
    if request.method != "POST":
        return render(request, 'mi_app/addPostulante.html')
    else:
        nombre_post=request.POST.get('nombre_post')
        numero_post=request.POST.get('numero_post')
        correo_post=request.POST.get('correo_post')
        ocupacion_post=request.POST.get('ocupacion_post')
        postulante=postulacion.objects.create(nombre_post=nombre_post,numero_post=numero_post,correo_post=correo_post,ocupacion_post=ocupacion_post)
        postulante.save()
        mensaje="postulante agregado con exito."
        context={'mensaje':mensaje}
        return render(request,'mi_app/tcn.html',context)
def delPostulante(request,pk):
    context={}
    try:
        postulante=postulacion.objects.get(id=pk)

        postulante.delete()
        mensaje="postulante eliminado con exito."
        postulantes=postulacion.objects.all()
        context = {'postulantes':postulantes, 'mensaje':mensaje}
        return redirect('crud')
    except:
        mensaje="postulante no encontrado"
        postulantes=postulacion.objects.all()
        context = {'postulantes':postulantes, 'mensaje':mensaje}
        return redirect('crud')

def findPostulante(request,pk):
    if pk != "":
        postulante=postulacion.objects.get(id=pk)
        context={'postulante':postulante}
        if postulante:
            return render(request,'mi_app/modPostulante.html',context)
        else:
            context={'mensaje':"Error, postulante no encontrado"}
            return redirect('crud')

def modPostulante(request):
    if request.method != "POST":
        return render(request, 'mi_app/modPostulante.html')
    else:
        id=request.POST.get('id_post')
        nombre_post=request.POST.get('nombre_post')
        numero_post=request.POST.get('numero_post')
        correo_post=request.POST.get('correo_post')
        ocupacion_post=request.POST.get('ocupacion_post')
        postulante=postulacion()
        postulante.id=id
        postulante.nombre_post=nombre_post
        postulante.numero_post=numero_post
        postulante.correo_post=correo_post
        postulante.ocupacion_post=ocupacion_post
        postulante.save()
        mensaje="postulante modificado con exito."
        context={'mensaje':mensaje}
        return redirect('crud')
