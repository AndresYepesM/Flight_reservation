from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings


# Create your models here.


class Flight(models.Model):

    flightNumber = models.CharField(max_length=10)
    operatinAirLines = models.CharField(max_length=20)
    departureCity = models.CharField(max_length=20, blank=True, null=True)
    arrivalCity = models.CharField(max_length=20)
    departure = models.DateField()
    estimatedTimeDepature = models.TimeField()


class Passenger(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    middle_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)


class Reservation(models.Model):
    fligth = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_authtoken(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
