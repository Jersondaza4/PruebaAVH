from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import csv
from .serializers import PokemonSerializer

class PokemonList(APIView):
    def get(self, request):
        pokemones = self.leer_pokemones()

        # Filtrar por tipo y/o número
        tipo = request.query_params.get('tipo')
        numero_mayor_que = request.query_params.get('numero_mayor_que')
        numero_menor_que = request.query_params.get('numero_menor_que')

        if tipo:
            pokemones = [p for p in pokemones if p['tipo'] == tipo]
        if numero_mayor_que:
            pokemones = [p for p in pokemones if int(p['numero']) > int(numero_mayor_que)]
        if numero_menor_que:
            pokemones = [p for p in pokemones if int(p['numero']) < int(numero_menor_que)]

        serializer = PokemonSerializer(pokemones, many=True)
        return Response(serializer.data)

    def leer_pokemones(self):
        pokemones = []
        with open('pokemones.csv', mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                pokemones.append(row)
        return pokemones

class PokemonCreate(APIView):
    def post(self, request):
        serializer = PokemonSerializer(data=request.data, many=True)
        if serializer.is_valid():
            self.escribir_pokemones(serializer.validated_data)
            return Response({"message": "Pokemones agregados correctamente!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def escribir_pokemones(self, pokemones):
        with open('pokemones.csv', mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['nombre', 'tipo', 'numero'])
            for pokemon in pokemones:
                writer.writerow(pokemon)