from rest_framework import viewsets, generics
from .models import (UserProfile, School, Subject, Teacher, ClassGroup, StudentProfile, Lesson,
                     Grade, QuarterGrade, Homework, Book, Attendance)
from .serializers import (UserProfileListSerializer, UserProfileDetailSerializer, UserProfileSimpleSerializer,
                          SchoolListSerializer, SchoolDetailSerializer, SubjectSerializer, TeacherSerializer,
                          ClassGroupListSerializer, ClassGroupDetailSerializer, StudentProfileSerializer, LessonListSerializer,
                          LessonDetailSerializer, GradeListSerializer, GradeDetailSerializer,
                          QuarterListGradeSerializer, QuarterDetailGradeSerializer,HomeworkSerializer, BookSerializer, AttendanceSerializer)

class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileListSerializer

class UserProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializer

class UserProfileSimpleAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSimpleSerializer

class SchoolListAPIViw(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolListSerializer

class SchoolCreateAPIView(generics.CreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolDetailSerializer

class SchoolDetailAPIViw(generics.RetrieveAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolDetailSerializer

class SchoolEditAPIViw(generics.DestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolDetailSerializer

class SubjectCreateAPIView(generics.CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class SubjectEditAPIView(generics.DestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class TeacherCreateAPIView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class ClassListAPIView(generics.ListAPIView):
    queryset = ClassGroup.objects.all()
    serializer_class = ClassGroupListSerializer

class ClassCreateAPIView(generics.CreateAPIView):
    queryset = ClassGroup.objects.all()
    serializer_class = ClassGroupDetailSerializer

class ClassEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassGroup.objects.all()
    serializer_class = ClassGroupDetailSerializer

class StudentProfileListAPIView(generics.ListAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer

class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer

class LessonDetailAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer

class LessonEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer

class GradeUpdateAPIView(generics.UpdateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeDetailSerializer

class GradeListAPIView(generics.ListAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeListSerializer

class GradeDetailAPIView(generics.RetrieveAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeDetailSerializer

class QuarterGradeListAPIView(generics.ListAPIView):
    queryset = QuarterGrade.objects.all()
    serializer_class = QuarterListGradeSerializer

class QuarterGradeDetailAPIView(generics.RetrieveAPIView):
    queryset = QuarterGrade.objects.all()
    serializer_class = QuarterDetailGradeSerializer

class QuarterGradeEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuarterGrade.objects.all()
    serializer_class = QuarterDetailGradeSerializer

class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer

class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookEditAPIView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AttendanceUpdateAPIView(generics.UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer