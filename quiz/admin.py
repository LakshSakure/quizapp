from django.contrib import admin
from .models import Student, Question, Quiz, School, Feedback
# Register your models here.

admin.site.register(Student)
admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(School)
admin.site.register(Feedback)