from django.urls import path
from . import views

urlpatterns = [
    path('add_student/', views.add_student, name='add'),
    path('students/<int:id>', views.students, name='students'),
    path('students/', views.students, name='students'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update')
    ]
