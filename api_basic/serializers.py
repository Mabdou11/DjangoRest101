from rest_framework import serializers
from .models import Alien, Box

class AlienSerializer(serializers.ModelSerializer):
    """
    a way to serialize the data to/from json
    """
    class Meta:
        model   = Alien
        fields  = ['id','name', 'planet', 'solarSystem', 'dateDiscovered','email', 'color', 'size', 'category' ]


class BoxSerializer(serializers.ModelSerializer):
    
    class Meta:
        model   = Box
        fields  = ['id', 'name', 'location', 'destination', 'weight']