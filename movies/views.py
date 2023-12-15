from django.shortcuts import render
from rest_framework import viewsets
from .serilizers import MovieSerializer
from .models import MovieData

# Création d'une vue en utilisant viewset de rest_framework
class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieSerializer
    queryset = MovieData.objects.all()

# Permet de classer et filtrer selon la catégorie
    # Action Category   
class ActionViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='action')
    serializer_class = MovieSerializer
    
    # Remonce Categorie
class RemonceViewSet(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(typ='Remonce')
    serializer_class = MovieSerializer