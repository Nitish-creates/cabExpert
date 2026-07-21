from django.urls import path
from . import views
urlpatterns = [
  path('createRide/ride',views.ride,name="ride")
]
