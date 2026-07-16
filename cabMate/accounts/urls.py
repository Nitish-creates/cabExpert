from . import views
from django.urls import path
urlpatterns = [
  path('login/',views.login_view,name='login'),
  path('register/',views.Register_view,name='register')
]
