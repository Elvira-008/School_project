from rest_framework import serializers
from .models import (UserProfile, School, Subject, Teacher, ClassGroup, StudentProfile, Lesson, Grade, QuarterGrade, Homework, Book, Attendance)
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'phone_number', 'login', 'create_at')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }

class UserProfileSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name']

class UserProfileListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'photo_profile', 'role', 'full_name']

class UserProfileDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', 'photo_profile', 'role', 'full_name', 'phone_number', 'login', 'create_at']

class SchoolListSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['name_school', 'address_school']

class SchoolDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['name_school', 'address_school', 'phonenumbers', 'create_at']

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['photo_subject', 'subject_name']


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id', 'teacher_name', 'subject_teacher', 'lesson']

class ClassGroupListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassGroup
        fields = ['id', 'class_name']

class ClassGroupDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassGroup
        fields = ['id', 'class_name', 'class_year']

class StudentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentProfile
        fields = ['id', 'user_student', 'class_group']

class LessonListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['subject', 'class_group', 'date', 'start_time', 'end_time']

class LessonDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['school', 'subject', 'class_group', 'date', 'start_time', 'end_time']

class GradeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'value_choices']

class GradeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'value_choices', 'teacher', 'created_at']

class QuarterListGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarterGrade
        fields = ['student', 'subject', 'quarter_choices', 'quarter_number']

class QuarterDetailGradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuarterGrade
        fields = ['student', 'subject', 'quarter_choices', 'quarter_number', 'school_year']

class HomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homework
        fields = ['lesson', 'title', 'file_url', 'deadline', 'created_at']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'author', 'subject', 'grade_level', 'file_url']

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['student', 'lesson', 'status', 'created_at', 'absent_time', 'present_time', 'late_minutes']
