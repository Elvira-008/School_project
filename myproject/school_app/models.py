from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MinValueValidator, MaxValueValidator


ROLE_CHOICES=(
("student","student"),
("teacher","teacher"),
("admin","admin"),
)

class UserProfile(AbstractUser):
    photo_profile = models.ImageField(upload_to='photo_profile/')
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="student")
    full_name = models.CharField(max_length=150)
    phone_number = PhoneNumberField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    login = models.CharField(max_length=64)
    create_register = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.full_name}, {self.role}'

    def save(self, *args, **kwargs):
        if self.password.startswith("S-"):
            self.role = "teacher"
        elif self.password.startswith("A-"):
            self.role = "admin"
        else:
            self.role = "student"
        super().save(*args, **kwargs)

class School(models.Model):
    name_school = models.CharField(max_length=255)
    address_school = models.TextField()
    phonenumbers = PhoneNumberField(null=True, blank=True)
    create_at = models.DateField()

    def __str__(self):
        return f'{self.name_school}'

class Subject(models.Model):
    photo_subject = models.ImageField(upload_to='photo_profile/')
    subject_name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.subject_name}'

class Teacher(models.Model):
    teacher_name = models.CharField(max_length=64)

    def __str__(self):
        return f'{self.teacher_name}'

class ClassGroup(models.Model):
    class_name = models.CharField(max_length=155, unique=True)
    class_year = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.class_name}'

class StudentProfile(models.Model):
    user_student = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    class_group = models.ForeignKey(ClassGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user_student}'

class Lesson(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_group = models.ForeignKey(ClassGroup, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

class Grade(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    VALUE_CHOICES = (
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    )
    value_choices = models.CharField(max_length=10, choices=VALUE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def predicted_quarter_grade(self):
        grades = Grade.objects.filter(student=self.student, subject=self.subject)
        if not grades.exists():
            return 0
        return round(sum(g.value_choices for g in grades) / grades.count(), 2)

class QuarterGrade(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    QUARTER_CHOICES = (
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    )
    quarter_choices = models.CharField(max_length=10, choices=QUARTER_CHOICES)
    final_grade = models.IntegerField()

class Homework(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    file_url = models.URLField(blank=True, null=True)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)


class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade_level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(11)])
    file_url = models.URLField()














