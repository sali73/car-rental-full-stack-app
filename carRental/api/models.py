from django.db import models

class Car(models.Model):
    model= models.CharField(max_length=10, null=True, blank=True)
    make = models.CharField(max_length=12, null=True, blank=True)
    color = models.CharField(max_length=10)
    year = models.CharField(max_length=400)
    seat_capacity = models.CharField(max_length=100, null=True, blank=True)
    photo = models.CharField(max_length=10, null=True, blank=True)
    rate = models.CharField(max_length=10, null=True, blank=True)
    current_mileage = models.CharField(max_length=50, null=True, blank=True)
    note = models.CharField(max_length=10, null=True, blank=True)

