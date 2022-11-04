from http.client import HTTPResponse
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth  import authenticate,  login, logout
from faculty.models import Faculty
from django.contrib.auth.models import Group
from quiz.models import Course

def FacultyLogin(request):
    if request.method=="POST":
        # Get the post parameters
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        
        print("loginusername: ",loginusername)
        
        user=authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            return redirect(facultyAfterLogin)
        else:
            
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

def facultyAfterLogin(request):
    return render(request,"faculty/facultyAfterlogin.html")



def CreateCourse(request):
    
    # return render(request,"faculty/createCourse.html")
    if request.method=="POST":
        Course_name=request.POST.get('Course_name', '')
        Course_dept=request.POST.get('Course_dept', '')
        Credit=request.POST.get("Credit",'') 
        
        print("Course_Name : ",Course_name)
        print("Department : ",Course_dept)
        print("Credit : ",Credit)
        course =Course(Course_name=Course_name,Course_dept=Course_dept,Credit=Credit)
        course.save()
        
    
        return render(request,"faculty/createCourse.html")   
    else:
        return render(request, "faculty/createCourse.html")
    
    
    #  class Quiz(models.Model):
    
    #     Quiz_id=models.AutoField(primary_key=True)
    #     Quiz_name=models.CharField(max_length=100)
    #     Quiz_Course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    #     Quiz_Faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    #     date=models.DateField(default=datetime.now)
    #     def __str__(self):
    #         return self.Quiz_name 
    
def CreateQuiz(request):
    
    # return render(request,"faculty/createCourse.html")
    if request.method=="POST":
        Quiz_name=request.POST.get('Quiz_name', '')
        Courses=request.POST.get('Course_name', '')
        date=request.POST.get("date",'') 
        
        Quiz_Course_id=Course.objects.filter(Course_name='DBMS').first
        Quiz_faculty=request.user
        
        print("Quiz_Course_id : ",Quiz_Course_id.Course_name)
        print("Course_name : ",Course)
        print("date : ",date)
        print("user is ",Quiz_faculty)
        course =Course(Course_name=Course,Quiz_Course_id=Quiz_Course_id,Quiz_faculty=Quiz_faculty,date=date)
        course.save()
        
    
        return render(request,"faculty/CreateQuiz.html")   
    else:
        return render(request, "faculty/CreateQuiz.html")