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
    path('register/', views.register, name='register')
]
