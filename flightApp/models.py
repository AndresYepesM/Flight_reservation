from django.db import models

# Create your models here.


class Flight(models.Model):

    flightNumber = models.CharField(max_length=10)
    operatinAirLines = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=20)
    arrivalCity = models.CharField(max_length=20)
    departure = models.DateField()
    estimatedTimeDepature = models.TimeField()


class Passenger(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=20)


class Reservation(models.Model):
    fligth = models.OneToOneField(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
