from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', auth_views.LogoutView.as_view(), name='profile'),
    path('add_student/', views.add_student, name='add'),
    path('students/<int:id>', views.students, name='students'),
    path('students/', views.students, name='students'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('register/', views.register, name='register'),
    path('add_course/', views.add_course, name='add_course'),
    path('courses/<int:code>', views.courses, name='courses'),
    path('courses/', views.courses, name='courses'),
    path('student_courses/', views.student_courses, name='student_courses'),
    path('reg_course/<int:code>/', views.reg_course, name='reg_course'),
    path('unreg_course/<int:code>/', views.unreg_course, name='unreg_course'),

]
