from django.db import models

# Create your models here.

class postulacion(models.Model):
    nombre_post = models.TextField(primary_key=True, max_length=50)
    correo_post = models.TextField(max_length=50)
    numero_post = models.IntegerField()
    ocupacion_post = models.TextField(max_length=200)