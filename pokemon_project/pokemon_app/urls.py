from django.urls import path
from .views import PokemonList, PokemonCreate

urlpatterns = [
    path('pokemones/', PokemonList.as_view(), name='pokemon-list'),
    path('pokemones/add/', PokemonCreate.as_view(), name='pokemon-create'),
]