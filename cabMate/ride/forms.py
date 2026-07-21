from django.forms import ModelForm
from .models import Ride

class RideForm(ModelForm):
    
    class Meta:
        model = Ride
        fields = ["pickup","destination","prefered_time","flexibility","max_seats"]
        

    