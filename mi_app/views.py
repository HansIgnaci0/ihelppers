from django.shortcuts import render

# Create your views here.

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