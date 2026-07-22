from django.urls import path
from . import views
urlpatterns = [
  path("create/", views.Create_ride_view, name="create_ride"),
]
