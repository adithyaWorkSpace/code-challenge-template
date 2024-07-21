from django.db import models


class weather_data(models.Model):
    filename = models.CharField(max_length=255)
    date = models.CharField(max_length=8)
    max_temp = models.IntegerField(null=True)
    min_temp = models.IntegerField(null=True)
    precipitation = models.IntegerField(null=True)

    
    class Meta:
        db_table = 'weather_data' 


class weather_stats(models.Model):
    year = models.CharField(max_length=8)
    filename = models.CharField(max_length=255)
    avg_max_temp = models.IntegerField(null=True)
    avg_min_temp = models.IntegerField(null=True)
    sum_precipitation = models.IntegerField(null=True)

    class Meta:
        db_table = 'weather_stats'
