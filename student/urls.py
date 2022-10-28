from django.contrib import admin
from django.urls import path,include

from . import views


urlpatterns = [
    path('',views.studentLogin,name='studentLogin'),
    path('temp',views.temp),
    path('studentRegister',views.studentRegister,name='studentRegister'),
    path('studentQuiz',views.studentQuiz,name='studentQuiz'),
]
