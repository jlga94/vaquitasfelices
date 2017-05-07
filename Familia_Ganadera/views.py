from django.shortcuts import render

from rest_framework import viewset
from Familia_Ganadera.models import Familia_Ganadera
from Familia_Ganadera.serializers import Familia_GanaderaSerializer

class Familia_GanaderaViewSet(viewsets.ModelViewSet):
    queryset = Familia_Ganadera.objects.all()
    serializer_class = Familia_GanaderaSerializer