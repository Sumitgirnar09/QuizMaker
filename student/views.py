from http.client import HTTPResponse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth  import authenticate,  login, logout
from student.models import Student
from django.contrib.auth.models import Group
from django.contrib import messages
from quiz.models import Quiz
from quiz.models import Result
quiz_dict={}


def studentLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        
        print("loginusername: ",loginusername)
        
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            return redirect("studentQuiz")
        else:
            # loginstatus={"valid":0}
            # return render(request,"student/studentlogin.html",loginstatus)
            return render(request,"student/studentlogin.html")

    return render(request,"student/studentlogin.html")

def studentRegister(request):
   
    if request.method=="POST":
        Name=request.POST.get('Name', '')
        Gender=request.POST.get("Gender",'')
        Year=request.POST.get("Year",'')
        Student_id=request.POST.get('Student_id','')
        Dob=request.POST.get('Dob','')
        print("Dob :",Dob)
        Dept=request.POST.get('Dept','')
        pass1=request.POST.get('pass1','')
        pass2=request.POST.get('pass2','')
        email=request.POST.get('email', '')
        
    
        student =Student(Name=Name,Student_id=Student_id,Gender=Gender,Dob=Dob,pass1=pass1,Year=Year,Dept=Dept,email=email)
        student.save()
        
        print("Name : ",Name)
        print("Gender : ",Gender)
        print("Year : ",Year)
        print("Student_id : ",Student_id)
        print("Dob : ",Dob)
        print("Dept : ",Dept)
        print("pass1 : ",pass1)
        print("pass2 : ",pass2)
        print("email : ",email)
        
        
        # Create the user
        myuser = User.objects.create_user(Student_id, email, pass1)
        myuser.save()
        my_group = Group.objects.get(name='student') 
        my_group.user_set.add(myuser)

        return redirect("studentLogin") 
        
        # return redirect('studenthome')
    else:
        return render(request, "student/studentregister.html")


def studentQuiz(request):
    
    quizzes_list=[]
    quizzes=Quiz.objects.all();
    print("quizzes ",quizzes)
    for quizz in quizzes:
        print("quizz ",quizz)
        quizzes_list.append(quizz)    
    quiz_dict["quizzes_list"]=quizzes_list
    return render(request,"student/studentQuiz.html",quiz_dict)

def AttemptQuiz(request):
    
    return render(request,"student/AttemptQuiz.html",quiz_dict)

def student_logout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect(studentLogin)