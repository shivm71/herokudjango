import math
import uuid

from django.db import models
from django.db.models import ForeignKey


class Driver(models.Model):
    driver_name = models.CharField(max_length=50)
    driver_mobile_no = models.CharField(max_length= 15)
    # car = models.ManyToManyField(Car, null=True, blank=True)
    # current_car = ForeignKey(Car)
    rating = models.FloatField()
    def __str__(self):
        return self.driver_name


class Car(models.Model):
    car_id = models.CharField(default=uuid.uuid1(),max_length=50)
    car_reg_no = models.CharField(max_length=50)
    current_x = models.FloatField()
    current_y = models.FloatField()
    driver = ForeignKey(Driver, on_delete=models.CASCADE)
    booked = models.BooleanField(default=False)

    # Home_position =
    def __str__(self):
        return self.car_reg_no


# accepted_pay_type =


class Ride(models.Model):
    ride_id = models.CharField(default=uuid.uuid1(),max_length=50)
    ride_start_time = models.DateTimeField(auto_now_add=True)
    ride_end_time = models.DateTimeField(auto_now_add=True)
    start_x = models.FloatField(default=0.00)
    start_y = models.FloatField(default=0.00)
    end_x = models.FloatField(default=0.00)
    end_y = models.FloatField(default=0.00)
    driver = ForeignKey(Driver, on_delete=models.CASCADE)
    car = ForeignKey(Car, on_delete=models.CASCADE)
    user_name = models.CharField(blank=True,max_length=50)
    fare = models.FloatField(default=0.00)
    status = models.CharField(default="Available",max_length=50)
    distance = models.FloatField(default=0.00)
    estimated_time = models.FloatField(blank=True)









# class BookingTable(models.Model):
#     id = models.CharField(default=uuid.uuid1())


class User(models.Model):
    user_id = models.CharField(default=uuid.uuid1(),max_length=50)
    user_name = models.CharField(max_length=100)
    # Payment_method =
    rides = models.ManyToManyField(Ride, null=True, blank=True)
