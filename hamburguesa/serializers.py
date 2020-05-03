from rest_framework import serializers
from .models import Hamburguesa, Ingrediente, IngredienteEnHamburguesa

class HamburguesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hamburguesa
        fields = ('id', 'nombre', 'precio', 'descripcion', 'imagen')

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = ('id', 'nombre', 'descripcion')

class IngredienteEnHamburguesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = IngredienteEnHamburguesa
        fields = ('hamburguesa_id', 'ingrediente_id')

