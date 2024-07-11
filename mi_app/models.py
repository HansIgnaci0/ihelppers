from django.db import models

# Create your models here.

class lenguaje(models.Model):
    idlenguaje = models.AutoField(db_column='id_lenguaje', primary_key=True)
    lenguaje = models.TextField(max_length=50, null=False)

class postulacion(models.Model):
    nombre_post = models.TextField(max_length=50)
    correo_post = models.TextField(max_length=50)
    numero_post = models.IntegerField()
    ocupacion_post = models.TextField(max_length=200)
    id_lenguaje = models.ForeignKey('lenguaje', on_delete=models.CASCADE, db_column='id_lenguaje')