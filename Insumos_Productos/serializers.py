from rest_framework import serializers
from Insumos_Productos.models import TipoInsumo, Insumo,TipoProductoIntermedio, ProductoIntermedio, TipoProductoFinal, ProductoFinal

class TipoInsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoInsumo
        fields = ('nombre', 'descripcion')

class InsumoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Insumo
        fields = ('lote', 'fecha_vencimiento', 'tipo_insumo')

class TipoProductoIntermedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProductoIntermedio
        fields = ('nombre', 'descripcion')

class ProductoIntermedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoIntermedio
        fields = ('lote', 'fecha_produccion', 'fecha_vencimiento', 'sigla', 'total', 'tipo_producto_intermedio')

class TipoProductoFinalerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProductoFinal
        fields = ('nombre', 'descripcion')

class ProductoFinalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductoFinal
        fields = ('lote', 'fecha_produccion', 'fecha_envasado', 'fecha_vencimiento', 'sigla', 'tipo_producto_final')

