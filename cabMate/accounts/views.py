from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username = username,password = password)
        
        if user is not None:
            login(request,user)
            messages.success(request,"Login successful")
            return redirect('home')
        else:
            messages.error(request,"Invalid username or Password")

    return render(request,'accounts/login.html')

def Register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirmPassword = request.POST.get('confirmPassword')
        context = {
            "username": username,
            "email": email,
            "phoneNumber": request.POST.get("phoneNumber"),
            "course": request.POST.get("course"),
            "year": request.POST.get("year"),
        }
        # checking passowrd
        if password != confirmPassword:
            messages.error(request,"Passwords Didn't match")
            return render(request,'accounts/register.html',context)
    
        # checking if email already registered
        if User.objects.filter(email=email).exists():
            messages.error(request,"Email already Exists")
            return render(request,'accounts/register.html',context)
        
        # checiking if username already exists
        if User.objects.filter(username = username).exists():
            messages.error(request,"Username Already Exits")
            return render(request,'accounts/register.html',context)
        
        # create the user 
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Account created successfully!")
        return redirect('login')
    
    return render(request,'accounts/register.html')



