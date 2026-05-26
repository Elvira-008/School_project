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
<<<<<<< HEAD
    login = models.CharField(max_length=64)
    create_register = models.DateTimeField(auto_now_add=True)#черновик
=======
    email = models.EmailField(null=True, blank=True)
    login = models.CharField(max_length=64)
    create_register = models.DateTimeField(auto_now_add=True)
>>>>>>> a3f4685408f1182b68358eb3169d9d32d815c96d

    def __str__(self):
        return f'{self.full_name}, {self.role}'

<<<<<<< HEAD
=======
    def save(self, *args, **kwargs):
        if self.password.startswith("S-"):
            self.role = "teacher"
        elif self.password.startswith("A-"):
            self.role = "admin"
        else:
            self.role = "student"
        super().save(*args, **kwargs)

>>>>>>> a3f4685408f1182b68358eb3169d9d32d815c96d
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
<<<<<<< HEAD
    subject_teacher = models.ForeignKey(Subject, on_delete=models.CASCADE)
=======
>>>>>>> a3f4685408f1182b68358eb3169d9d32d815c96d

    def __str__(self):
        return f'{self.teacher_name}'

class ClassGroup(models.Model):
    class_name = models.CharField(max_length=155, unique=True)
    class_year = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.class_name}'

<<<<<<< HEAD


=======
>>>>>>> a3f4685408f1182b68358eb3169d9d32d815c96d
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

<<<<<<< HEAD
    def __str__(self):
        return f'{self.subject.subject_name}'

=======
>>>>>>> a3f4685408f1182b68358eb3169d9d32d815c96d
class Grade(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    VALUE_CHOICES = (
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
<<<<<<< HEAD
    ('H', 'H'),
    ('Нб', 'Нб')
=======
>>>>>>> a3f4685408f1182b68358eb3169d9d32d815c96d
    )
    value_choices = models.CharField(max_length=10, choices=VALUE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

<<<<<<< HEAD
    def __str__(self):
        return f'{self.student.full_name}'

=======
>>>>>>> a3f4685408f1182b68358eb3169d9d32d815c96d
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
<<<<<<< HEAD

    def __str__(self):
        return f'{self.student.full_name}'
=======
    final_grade = models.IntegerField()
>>>>>>> a3f4685408f1182b68358eb3169d9d32d815c96d

class Homework(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    file_url = models.URLField(blank=True, null=True)
<<<<<<< HEAD
    deadline = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

=======
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

>>>>>>> a3f4685408f1182b68358eb3169d9d32d815c96d

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade_level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(11)])
    file_url = models.URLField()

<<<<<<< HEAD
    def __str__(self):
        return f'{self.title}'

class Message(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    message = models.TextField()
    file = models.FileField(upload_to='file/')
    voice = models.FileField(upload_to='voices/')
    sticker = models.FileField(upload_to='stickers/')
    message_date = models.DateTimeField(auto_now_add=True)

class Chat(models.Model):
    admin = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='admin')
    user = models.ManyToManyField(UserProfile, related_name='user')
    group_name = models.CharField(max_length=64)
    group_image = models.ImageField(upload_to='group_image/')
    class_chat = models.ForeignKey(ClassGroup, on_delete=models.CASCADE)
    create_group = models.DateTimeField(auto_now_add=True)


=======
>>>>>>> a3f4685408f1182b68358eb3169d9d32d815c96d













