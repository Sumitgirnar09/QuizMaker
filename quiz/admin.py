from django.contrib import admin
from .models import Course,Question,Quiz,Result

# Register your models here.
admin.site.register(Course)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Result)