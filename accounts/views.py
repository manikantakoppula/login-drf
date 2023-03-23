from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        uName= request.POST['username']
        password1= request.POST['password1']
        password2= request.POST['password2']
        email= request.POST['email']
        if password1 == password2:
            if User.objects.filter(username=uName).exists():
                messages.info(request,"username Exists")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email Exists")
                return redirect('register')           
            else:
                user = User.objects.create_user(email=email,password=password1,username=uName)
                user.save()
                return redirect('/')
        else:
            messages.info(request,"password not matching")
            return redirect('register') 
    else:    
        return render(request,'registrations/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password=request.POST['password']
        user =authenticate(request,username=username,password=password)
        if user:
            login(request,user)
            return redirect('/index/')
        else:
            messages.info(request,"username or password invaild")
            return render(request,'logins/login.html')
    else:
        return render(request,'logins/login.html')

def user_logout(request):
    logout(request)
    messages.success(request,"logout")
    return redirect('accounts:login')

