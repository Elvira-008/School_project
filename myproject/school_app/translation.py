from .models import UserProfile, School, Subject, Homework, Book
from modeltranslation.translator import TranslationOptions,register

@register(UserProfile)
class UserProfileTranslationOptions(TranslationOptions):
    fields = ('full_name', )

@register(School)
class SchoolTranslationOptions(TranslationOptions):
    fields = ('name_school', 'address_school')

@register(Subject)
class SubjectTranslationOptions(TranslationOptions):
    fields = ('subject_name', )

@register(Homework)
class HomeworkTranslationOptions(TranslationOptions):
    fields = ('title', )

@register(Book)
class BookTranslationOptions(TranslationOptions):
    fields = ('author', 'title')
