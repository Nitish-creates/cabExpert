from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Ride(models.Model):
    FLEXIBILITY_CHOICES = [
        ('5','5 minutes'),
        ('10','10 minutes'),
        ('15','15 minutes'),
    ]
    creator = models.ForeignKey(User,on_delete = models.CASCADE)
    pickup = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    prefered_time = models.DateTimeField()
    flexibility = models.IntegerField(choices=FLEXIBILITY_CHOICES)
    max_seats = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add= True)
    def __str__(self):
        return f"{self.pickup} → {self.destination}"
    
class Ride_member(models.Model):
    