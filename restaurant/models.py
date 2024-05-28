from django.db import models

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=200)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()

class Menu(models.Model):
    Title = models.CharField(max_length=100)
    Price = models.IntegerField()
    Inventory = models.IntegerField()