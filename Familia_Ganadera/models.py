from django.db import models

# Create your models here.

class Familia_Ganadera(models.Model):
	dni = models.CharField(max_length=10)
	nombre = models.CharField(max_length=25)
	apellido_paterno = models.CharField(max_length=25)
	apellido_materno = models.CharField(max_length=25)
	altitud  = models.CharField(max_length=25)
	provincia = models.CharField(max_length=25)
	distrito = models.CharField(max_length=25)
	lugar = models.CharField(max_length=25)
	telefono = models.CharField(max_length=15)
	celular = models.CharField(max_length=15)
	fecha_nacimiento = models.DateField(null=True,blank=True)

