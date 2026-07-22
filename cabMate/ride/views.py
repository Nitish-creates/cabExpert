from django.shortcuts import render,redirect
from .models import Ride,Ride_member
from .forms import RideForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
# Create your views here.
def Create_ride_view(request):
    if request.method == 'GET':
      form = RideForm()
      return render(request, "ride/create_ride.html", {"form": form})
    if request.method == 'POST':
      form = RideForm(request.POST)
      if form.is_valid():
        pickup = form.cleaned_data['pickup']
        destination = form.cleaned_data['destination']
        preferred_time = form.cleaned_data['preferred_time']
        flexibility = form.cleaned_data['flexibility']

        # checking destination or pickup
        if pickup == destination:
           messages.error(request,"pickup and destination is same please enter valid destination")
           return render(request, "ride/create_ride.html", {"form": form})
        
        # checking time   
        current_time = timezone.now()   
        if (preferred_time + timedelta(minutes=flexibility)) < current_time:
           messages.error(request,"Ride time cannot be in the past.")
           return render(request, "ride/create_ride.html", {"form": form})
        ride = form.save(commit=False)
        ride.creator = request.user
        ride.save()
        messages.success(request,"Ride Created Successfully")
        return redirect('home')

def find_ride_view(request):
   rides = Ride.objects.all()        