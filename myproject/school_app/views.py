from rest_framework import viewsets, generics
from .models import (UserProfile, School, Subject, Teacher, ClassGroup,StudentProfile, Lesson, Grade, QuarterGrade,Homework, Book, Attendance)
from .permissions import (IsTeacher, IsAdmin, IsOwnerOrAdmin,IsTeacherOfLesson, IsAdminOrTeacher)
from .serializers import (
    UserProfileListSerializer, UserProfileDetailSerializer, UserProfileSimpleSerializer,
    SchoolListSerializer, SchoolDetailSerializer,
    SubjectSerializer, TeacherSerializer,
    ClassGroupListSerializer, ClassGroupDetailSerializer,
    StudentProfileSerializer,
    LessonListSerializer, LessonDetailSerializer,
    GradeListSerializer, GradeDetailSerializer,
    QuarterListGradeSerializer, QuarterDetailGradeSerializer,
    HomeworkSerializer, BookSerializer, AttendanceSerializer)

class UserProfileListAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileListSerializer

class UserProfileDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileDetailSerializer
    permission_classes = [IsOwnerOrAdmin]

class UserProfileSimpleAPIView(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSimpleSerializer

class SchoolListAPIView(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolListSerializer

class SchoolCreateAPIView(generics.CreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolDetailSerializer
    permission_classes = [IsAdmin]

class SchoolDetailAPIView(generics.RetrieveAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolDetailSerializer
    permission_classes = [IsAdmin]

class SchoolEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolDetailSerializer
    permission_classes = [IsAdmin]

class SubjectCreateAPIView(generics.CreateAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAdmin]

class SubjectEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAdmin]

class TeacherCreateAPIView(generics.CreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdmin]

class TeacherEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAdmin]

class ClassListAPIView(generics.ListAPIView):
    queryset = ClassGroup.objects.all()
    serializer_class = ClassGroupListSerializer

class ClassCreateAPIView(generics.CreateAPIView):
    queryset = ClassGroup.objects.all()
    serializer_class = ClassGroupDetailSerializer
    permission_classes = [IsAdmin]

class ClassEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClassGroup.objects.all()
    serializer_class = ClassGroupDetailSerializer
    permission_classes = [IsAdmin]

class StudentProfileListAPIView(generics.ListAPIView):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer
    permission_classes = [IsOwnerOrAdmin]

class LessonListAPIView(generics.ListAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonListSerializer

class LessonDetailAPIView(generics.RetrieveAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer

class LessonEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonDetailSerializer
    permission_classes = [IsTeacherOfLesson]

class GradeListAPIView(generics.ListAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeListSerializer
    permission_classes = [IsTeacherOfLesson]



class GradeDetailAPIView(generics.RetrieveAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeDetailSerializer
    permission_classes = [IsTeacherOfLesson]

class GradeUpdateAPIView(generics.UpdateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeDetailSerializer
    permission_classes = [IsTeacher]

class QuarterGradeListAPIView(generics.ListAPIView):
    queryset = QuarterGrade.objects.all()
    serializer_class = QuarterListGradeSerializer
    permission_classes = [IsTeacher]


class QuarterGradeDetailAPIView(generics.RetrieveAPIView):
    queryset = QuarterGrade.objects.all()
    serializer_class = QuarterDetailGradeSerializer
    permission_classes = [IsTeacher]


class QuarterGradeEditAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuarterGrade.objects.all()
    serializer_class = QuarterDetailGradeSerializer
    permission_classes = [IsTeacher]


class HomeworkViewSet(viewsets.ModelViewSet):
    queryset = Homework.objects.all()
    serializer_class = HomeworkSerializer
    permission_classes = [IsTeacherOfLesson]

class BookCreateAPIView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrTeacher]

class BookEditAPIView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminOrTeacher]

class AttendanceListAPIView(generics.ListAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsTeacherOfLesson]

class AttendanceUpdateAPIView(generics.UpdateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [IsTeacher]
