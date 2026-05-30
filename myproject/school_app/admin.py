from django.contrib import admin
from .models import (UserProfile, School, Subject, Teacher, ClassGroup,
                     StudentProfile, Lesson, QuarterGrade, Homework, Book, Attendance, Grade)

admin.site.register(UserProfile)
admin.site.register(School)
admin.site.register(Subject)
admin.site.register(Teacher)
admin.site.register(ClassGroup)
admin.site.register(StudentProfile)
admin.site.register(Lesson)
admin.site.register(QuarterGrade)
admin.site.register(Homework)
admin.site.register(Book)
admin.site.register(Attendance)
admin.site.register(Grade)

