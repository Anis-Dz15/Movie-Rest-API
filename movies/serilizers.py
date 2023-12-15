from rest_framework import serializers
from .models import MovieData

# Initialisation du Serilizer
class MovieSerializer(serializers.ModelSerializer):
    # initialiser l'ajout d'image dans le serializer 
        # Spécifier que la taille est null
        # Spécifier que l'image contient un chemin ( chemin dans lequel elle a été sauvgardée )
    image = serializers.ImageField(max_length=None,use_url=True)
    class Meta:
        model = MovieData
        fields = ['id','name','duration','rating','typ','image']