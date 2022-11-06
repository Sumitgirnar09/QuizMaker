from django.contrib import admin
from django.urls import path,include

from . import views


urlpatterns = [
    path('',views.studentLogin,name='studentLogin'),
    path('studentRegister/',views.studentRegister,name='studentRegister'),
    path('studentQuiz/',views.studentQuiz,name='studentQuiz'),
    path('AttemptQuiz',views.AttemptQuiz,name='AttemptQuiz'),
    path('GenerateResult',views.GenerateResult,name='GenerateResult'),
    path('student_logout/',views.student_logout,name='student_logout'),
    path('grades/',views.grades,name='grades'),
]
