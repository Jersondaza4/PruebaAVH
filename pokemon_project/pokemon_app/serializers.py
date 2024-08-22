from rest_framework import serializers

class PokemonSerializer(serializers.Serializer):
    nombre = serializers.CharField(max_length=100)
    tipo = serializers.CharField(max_length=50)
    numero = serializers.IntegerField()