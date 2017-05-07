from django.shortcuts import render

from rest_framework import viewset
from Porongo.models import Porongo
from Porongo.serializers import PorongoSerializer

class Familia_GanaderaViewSet(viewsets.ModelViewSet):
    queryset = Porongo.objects.all()
    serializer_class = PorongoSerializer