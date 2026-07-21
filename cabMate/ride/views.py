from django.shortcuts import render
from .models import Ride,Ride_member
# Create your views here.
def ride(request):
    return render(request,'ride.html')
