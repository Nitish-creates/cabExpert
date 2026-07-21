from django.http import HttpResponse

def home(request):
    return HttpResponse('welcome to the home page')

def myRide(request):
    return HttpResponse('welcome to the MY- ride page')

def CreateRide(request):
    return HttpResponse('welcome to the Create-ride ')

def JoinRide(request):
    return HttpResponse('welcome to the join ride')