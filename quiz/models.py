from ast import Pass
from asyncio.windows_events import NULL
from curses.ascii import NUL
from datetime import datetime
import email
from email.policy import default
from random import choices
from django.db import models
from faculty.models import Faculty
from student.models import Student
# Create your models here.

class Course(models.Model):
    
    Course_id = models.AutoField(primary_key=True)
    Course_name = models.CharField(max_length=50)
    Course_dept=models.CharField(max_length=100)
    Credit=models.CharField(max_length=100,default=NULL)
    def __str__(self):
        return self.Course_name

class Quiz(models.Model):
    
    Quiz_id=models.AutoField(primary_key=True)
    Quiz_name=models.CharField(max_length=100)
    Quiz_Course_id = models.ForeignKey(Course,on_delete=models.CASCADE)
    Quiz_Faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    date=models.DateField(default=datetime.now)
    def __str__(self):
        return self.Quiz_name

class Question(models.Model):
    
    Question_id=models.AutoField(primary_key=True)
    Question_quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    Question_desc=models.CharField(max_length=100)
    marks=models.IntegerField()
    neg_marks=models.IntegerField()
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    correct_option=models.IntegerField()
    
    def __str__(self):
        return self.Question_quiz.Quiz_name+"("+str(self.Question_id)+")"
    
class Result(models.Model):
    STATUS = (
    ("P", "Pass"),
    ("F", "Fail"),
    )
    Result_id=models.AutoField(primary_key=True)
    Quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    marks=models.IntegerField()
    status=models.CharField(max_length=50,choices=STATUS,default=NULL)

