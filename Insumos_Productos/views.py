from django.shortcuts import render

from rest_framework import viewset
from Insumos_Productos.models import TipoInsumo, Insumo,TipoProductoIntermedio, ProductoIntermedio, TipoProductoFinal, ProductoFinal
from Insumos_Productos.serializers import TipoInsumoSerializer,InsumoSerializer, TipoProductoIntermedioSerializer, ProductoIntermedioSerializer, TipoProductoFinalSerializer, ProductoFinalSerializer

class TipoInsumoViewSet(viewsets.ModelViewSet):
    queryset = TipoInsumo.objects.all()
    serializer_class = TipoInsumoSerializer

class InsumoViewSet(viewsets.ModelViewSet):
    queryset = Insumo.objects.all()
    serializer_class = InsumoSerializer

class TipoProductoIntermedioViewSet(viewsets.ModelViewSet):
    queryset = TipoProductoIntermedio.objects.all()
    serializer_class = TipoProductoIntermedioSerializer

class ProductoIntermedioViewSet(viewsets.ModelViewSet):
    queryset = ProductoIntermedio.objects.all()
    serializer_class = ProductoIntermedioSerializer

class TipoProductoFinalViewSet(viewsets.ModelViewSet):
    queryset = TipoProductoFinal.objects.all()
    serializer_class = TipoProductoFinalSerializer

class ProductoFinalViewSet(viewsets.ModelViewSet):
    queryset = ProductoFinal.objects.all()
    serializer_class = ProductoFinalSerializer
