from django.contrib import admin
from rest_framework.exceptions import ValidationError

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

<<<<<<< HEAD
def check_admin_limit(obj, limit_minutes):
    from django.utils import timezone

    if obj.created_at and timezone.now() > obj.created_at + timezone.timedelta(minutes=limit_minutes):
        raise ValidationError("Нельзя изменять посещаемость")


=======
>>>>>>> 92bb04a76d163e55b06def5df347087c4d94dda9
