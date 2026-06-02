from django.contrib import admin
from .models import (UserProfile, School, Subject, Teacher, ClassGroup,
                     StudentProfile, Lesson, QuarterGrade, Homework, Book, Attendance, Grade)
from modeltranslation.admin import TranslationAdmin

@admin.register(UserProfile, School, Subject, Homework, Book)
class AllAdmin(TranslationAdmin):
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(Teacher)
admin.site.register(ClassGroup)
admin.site.register(StudentProfile)
admin.site.register(Lesson)
admin.site.register(QuarterGrade)
admin.site.register(Attendance)
admin.site.register(Grade)


