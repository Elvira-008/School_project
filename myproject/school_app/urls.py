from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (UserProfileListAPIView, UserProfileDetailAPIView, UserProfileSimpleAPIView,
                    SchoolListAPIView, SchoolCreateAPIView, SchoolDetailAPIView, SchoolEditAPIView,
                    SubjectCreateAPIView, SubjectEditAPIView, TeacherCreateAPIView, TeacherEditAPIView,
                    ClassListAPIView, ClassCreateAPIView, ClassEditAPIView, StudentProfileListAPIView,
                    LessonListAPIView, LessonDetailAPIView, LessonEditAPIView, GradeListAPIView,
                    GradeDetailAPIView, GradeUpdateAPIView, QuarterGradeListAPIView, QuarterGradeDetailAPIView,
                    QuarterGradeEditAPIView, HomeworkViewSet, BookCreateAPIView, BookEditAPIView,
                    AttendanceUpdateAPIView, AttendanceListAPIView, RegisterView, CustomLoginView, LogoutView)

router = SimpleRouter()
router.register(r'homeworks', HomeworkViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('users/', UserProfileListAPIView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserProfileDetailAPIView.as_view(), name='user-detail'),
    path('users/simple/', UserProfileSimpleAPIView.as_view(), name='user-simple'),
    path('schools/', SchoolListAPIView.as_view(), name='school-list'),
    path('schools/create/', SchoolCreateAPIView.as_view(), name='school-create'),
    path('schools/<int:pk>/', SchoolDetailAPIView.as_view(), name='school-detail'),
    path('schools/<int:pk>/delete/', SchoolEditAPIView.as_view(), name='school-delete'),
    path('subjects/create/', SubjectCreateAPIView.as_view(), name='subject-create'),
    path('subjects/<int:pk>/delete/', SubjectEditAPIView.as_view(), name='subject-delete'),
    path('teachers/create/', TeacherCreateAPIView.as_view(), name='teacher-create'),
    path('teachers/<int:pk>/', TeacherEditAPIView.as_view(), name='teacher-edit'),
    path('classes/', ClassListAPIView.as_view(), name='class-list'),
    path('classes/create/', ClassCreateAPIView.as_view(), name='class-create'),
    path('classes/<int:pk>/', ClassEditAPIView.as_view(), name='class-edit'),
    path('students/', StudentProfileListAPIView.as_view(), name='student-list'),
    path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonDetailAPIView.as_view(), name='lesson-detail'),
    path('lessons/<int:pk>/edit/', LessonEditAPIView.as_view(), name='lesson-edit'),
    path('grades/', GradeListAPIView.as_view(), name='grade-list'),
    path('grades/<int:pk>/', GradeDetailAPIView.as_view(), name='grade-detail'),
    path('grades/<int:pk>/update/', GradeUpdateAPIView.as_view(), name='grade-update'),
    path('quarter-grades/', QuarterGradeListAPIView.as_view(), name='quarter-grade-list'),
    path('quarter-grades/<int:pk>/', QuarterGradeDetailAPIView.as_view(), name='quarter-grade-detail'),
    path('quarter-grades/<int:pk>/edit/', QuarterGradeEditAPIView.as_view(), name='quarter-grade-edit'),
    path('books/create/', BookCreateAPIView.as_view(), name='book-create'),
    path('books/<int:pk>/', BookEditAPIView.as_view(), name='book-edit'),
    path('attendance/', AttendanceListAPIView.as_view(),name='attendance-list'),
    path('attendance/<int:pk>/update/', AttendanceUpdateAPIView.as_view(), name='attendance-update'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]