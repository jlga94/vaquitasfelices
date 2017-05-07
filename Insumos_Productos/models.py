from django.db import models

class TipoInsumo(models.Model):
	nombre = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=100)

class Insumo(models.Model):
	lote = models.CharField(max_length=20)
	fecha_vencimiento = models.DateField(null=True,blank=True)
	tipo_insumo = models.ForeignKey(TipoInsumo)


class TipoProductoIntermedio(models.Model):
	nombre = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=100)

class ProductoIntermedio(models.Model):
	lote = models.CharField(max_length=20)
	fecha_produccion = models.DateField(null=True,blank=True)
	fecha_vencimiento = models.DateField(null=True,blank=True)
	sigla = models.CharField(max_length=10)
	total = models.FloatField()
	tipo_producto_intermedio = models.ForeignKey(TipoProductoIntermedio)

class TipoProductoFinal(models.Model):
	nombre = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=100)

class ProductoFinal(models.Model):
	lote = models.CharField(max_length=20)
	fecha_produccion = models.DateField(null=True,blank=True)
	fecha_envasado = models.DateField(null=True,blank=True)
	fecha_vencimiento = models.DateField(null=True,blank=True)
	sigla = models.CharField(max_length=10)
	tipo_producto_final= models.ForeignKey(TipoProductoFinal)