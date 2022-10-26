from http.client import HTTPResponse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth  import authenticate,  login, logout

def home(request):
    return render(request,'admin/home.html')

def AdminLogin(request):
    # return HttpResponse("Admin Login Entered")
    # return render(request,'admin/adminLogin.html')
    
    if request.method=="POST":
        
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        loginemail=request.POST['loginemail']
        
        # print("loginusername : ",loginusername)
        # print("loginpassword : ",loginpassword)
        
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None and request.user.is_superuser:
            login(request, user)
            return HttpResponse("Superuser Logged In")
            # return render(request,"admin/adminLogin.html")
        else:
            # loginstatus={"valid":0}
            # return render(request,"student/home.html",loginstatus)
            return HttpResponse("You are not allowed to visit this page")
    
    return render(request,"admin/adminLogin.html")
