from django.contrib import admin
from django.urls import path,include

from . import views


urlpatterns = [
    path('',views.FacultyLogin,name='FacultyLogin'),
    path('facultyRegister/',views.facultyRegister,name='facultyRegister'),
    path('facultyAfterLogin/',views.facultyAfterLogin,name='facultyAfterLogin'),
    path('facultyAfterLogin/CreateCourse/',views.CreateCourse,name='CreateCourse'),
    # path('studentQuiz',views.studentQuiz,name='studentQuiz'),
]
