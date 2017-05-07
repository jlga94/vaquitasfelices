from django.db import models
from Familia_Ganadera.models import Familia_Ganadera

# Create your models here.
class Porongo(models.Model):
	fecha_ingreso = models.DateField(null=True,blank=True)
	EsDeCalidad = models.BooleanField()
	asignacion_ticket = models.BooleanField()
	EsOrganica = models.BooleanField()
	cantidad = models.FloatField()
	cvIcual = models.CharField(max_length=50)
	calidad = models.CharField(max_length=50)
	observaciones = models.CharField(max_length=200)
	medidaCorrectiva  = models.CharField(max_length=150)
	familia_ganadera = models.ForeignKey(Familia_Ganadera)