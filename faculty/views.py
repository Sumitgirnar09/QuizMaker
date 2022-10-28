from http.client import HTTPResponse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth  import authenticate,  login, logout
from faculty.models import Faculty
from django.contrib.auth.models import Group

def FacultyLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        
        print("loginusername: ",loginusername)
        
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            print("Faculty ",loginusername," logged in")
            # return render(request,"faculty/QuizCreate.html")
        else:
            # loginstatus={"valid":0}
            # return render(request,"student/studentlogin.html",loginstatus)
            return render(request,"faculty/facultylogin.html")

    return render(request,"faculty/facultylogin.html")

def facultyRegister(request):
   
    if request.method=="POST":
        First_Name=request.POST.get('First_Name', '')
        Last_Name=request.POST.get('Last_Name', '')
        Gender=request.POST.get("Gender",'')
        Dob=request.POST.get('Dob','')
        Dept=request.POST.get('Dept','')
        pass1=request.POST.get('pass1','')
        pass2=request.POST.get('pass2','')
        email=request.POST.get('email', '')
        
    
        faculty =Faculty(First_Name=First_Name,Last_Name=Last_Name,Gender=Gender,Dob=Dob,pass1=pass1,pass2=pass2,Dept=Dept,email=email)
        faculty.save()
        
        print("First_Name : ",First_Name)
        print("Last_Name : ",Last_Name)
        print("Gender : ",Gender)
        print("Dob : ",Dob)
        print("Dept : ",Dept)
        print("pass1 : ",pass1)
        print("pass2 : ",pass2)
        print("email : ",email)
        
        
        # Create the user
        myuser = User.objects.create_user(email, email, pass1)
        myuser.save()
        my_group = Group.objects.get(name='faculty') 
        my_group.user_set.add(myuser)

        return render(request,"faculty/facultyregister.html")   
        
        # return redirect('studenthome')
    else:
        return render(request, "faculty/facultyregister.html")

