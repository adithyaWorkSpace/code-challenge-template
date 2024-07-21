"""
Serializers for the Weather Data and Weather Statistics models.

This module contains the serializers for converting 
WeatherData and WeatherStats model instances into JSON 
format and vice versa. It uses Django REST Framework's 
ModelSerializer to handle the serialization and deserialization 
of model instances.
"""
from rest_framework import serializers
from .models import weather_data, weather_stats

class WeatherDataSerializer(serializers.ModelSerializer):
    """Serializer for WeatherData model."""
    class Meta:
        model = weather_data
        fields = '__all__'

class WeatherStatsSerializer(serializers.ModelSerializer):
    """Serializer for WeatherStats model."""
    class Meta:
        model = weather_stats
        fields = '__all__'
