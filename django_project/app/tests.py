from django.test import TestCase, Client
from rest_framework import status
from app.models import weather_data, weather_stats


class WeatherDataAndStatsTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.weather_data_1 = weather_data.objects.create(
            filename="USC00259510",
            date="19850101",
            max_temp=-78,
            min_temp=-206,
            precipitation=0
        )
        self.weather_data_2 = weather_data.objects.create(
            filename="USC00126580",
            date="19850101",
            max_temp=178,
            min_temp=83,
            precipitation=279
        )
        self.weather_stats_1 = weather_stats.objects.create(
            year="1985",
            filename="USC00119241",
            avg_max_temp=161,
            avg_min_temp=47,
            sum_precipitation=12130
        )
        self.weather_stats_2 = weather_stats.objects.create(
            year="1985",
            filename="USC00121425",
            avg_max_temp=179,
            avg_min_temp=64,
            sum_precipitation=8509
        )

    def test_get_weather_data(self):
        response = self.client.get('/api/weather/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.json().get("results", [])
        self.assertGreater(len(results), 0)
        self.assertIn("USC00259510", [data['filename'] for data in results])
        self.assertIn("USC00126580", [data['filename'] for data in results])

    def test_get_weather_data_stats(self):
        response = self.client.get('/api/weather/stats/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.json().get("results", [])
        self.assertGreater(len(results), 0)
        self.assertIn("USC00119241", [data['filename'] for data in results])
        self.assertIn("USC00121425", [data['filename'] for data in results])
