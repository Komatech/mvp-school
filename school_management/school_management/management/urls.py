from django.contrib import admin
from django.urls import path
from management import views


urlpatterns = [
    # path('', views.profile,name='staff_home'),
    path('students/', views.best_student,name='studentslist'),
    path('subject/', views.best_student_subject,name='subjects'),
    path('student_no/', views.total_students,name='total_students'),
    # path('create_student/', views.create_student,name='create_student'),
    # path('create_staff/', views.create_staff,name='create_staff'),
    # path('update_student/<str:pk>', views.update_student,name='update_student'),
    path('staff/', views.total_staff,name='total_staff'),
    # path('update_staff/<str:pk>', views.update_staff,name='update_student'),
]