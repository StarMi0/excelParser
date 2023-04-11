from django.db import models
from datetime import datetime


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.CharField(max_length=255)
    fact_qliq = models.IntegerField()
    fact_qoil = models.IntegerField()
    forecast_qliq = models.IntegerField()
    forecast_qoil = models.IntegerField()
    fact_qliq_2 = models.IntegerField()
    fact_qoil_2 = models.IntegerField()
    forecast_qliq_2 = models.IntegerField()
    forecast_qoil_2 = models.IntegerField()
    date = models.DateField(default=datetime(2022, 6, 1))
