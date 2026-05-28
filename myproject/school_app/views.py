from rest_framework import viewsets
from .models import (UserProfile, School, Subject, Teacher, ClassGroup, StudentProfile, Lesson,
                     Grade, QuarterGrade, Homework, Book)
from .serializers import (UserProfileSerializer, SchoolSerializer, SubjectSerializer, TeacherSerializer,
                          ClassGroupSerializer, StudentProfileSerializer, LessonSerializer, GradeSerializer,
                          QuarterGradeSerializer, HomeworkSerializer, BookSerializer)

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class SchoolViwSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class ClassGroupViewSet(viewsets.ModelViewSet):
    queryset = ClassGroup.objects.all()
    serializer_class = ClassGroupSerializer

class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class GradeViewsSet(viewsets.ModelViewSet):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer

class QuarterGradeViewSet(viewsets.ModelViewSet):
    queryset = QuarterGrade.objects.all()
    serializer_class = QuarterGradeSerializer

class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer