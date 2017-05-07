from rest_framework import serializers
from Familia_Ganadera.models import Familia_Ganadera

class Familia_GanaderaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Familia_Ganadera
        fields = ('dni', 'nombre', 'apellido_paterno', 'apellido_materno', 'altitud', 'provincia', 'distrito', 'lugar', 'telefono', 
		'celular', 'fecha_nacimiento')
