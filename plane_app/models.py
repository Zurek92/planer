from django.db import models

from choices import choices

# Create your models here.
class AirCompany(models.Model):
    air_company = models.CharField(max_length=50)
    flight_number = models.CharField(max_length=10)
    flight_status = models.CharField(choices=choices, default = ('on_time','on_time'))
    amount_of_delayed_flights_by_air_company = models.IntegerField()
    amount_of_cancelled_flights_by_air_company = models.IntegerField()
    amount_of_total_flights_by_air_company = models.IntegerField()

class Airport(models.Model):
    airport_name = models.CharField(max_length=50)
    # 3 letters code in IATA system ie. KRK, GDN
    airport_code = models.CharField(max_length=3)
    air_company = models.ManyToManyField(AirCompany)
    flight_number = models.ManyToManyField(AirCompany)
    flight_status = models.ManyToManyField(AirCompany)
    #arrival flights should have 1 as integer and departure flights should have 2
    kind_of_flight = models.IntegerField(max_length=1)
    amount_delayed_flights_on_airport = models.IntegerField()
    amount_cancelled_flights_on_airport = models.IntegerField()
    total_flights_on_airport = models.IntegerField()
 
