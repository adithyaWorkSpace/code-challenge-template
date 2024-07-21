""" 
    This module contains views for weather_info
"""
import logging
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from .models import weather_stats, weather_data
from .serializers import WeatherDataSerializer, WeatherStatsSerializer

logger=logging.getLogger(__name__)


class WeatherDataList(generics.ListAPIView):
    queryset = weather_data.objects.all()
    print(weather_data.objects.all())
    serializer_class = WeatherDataSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date', 'filename']

class WeatherStatsList(generics.ListAPIView):
    queryset = weather_stats.objects.all()
    serializer_class = WeatherStatsSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['year', 'filename']