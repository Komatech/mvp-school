from django.contrib import admin
from django.urls import path
from Admin import views


urlpatterns = [
    # path('', views.profile,name='staff_home'),
    path('students/', views.studentprofile,name='studentslist'),
    path('staffs/', views.staffprofile,name='stafflist'),
    path('create_student/', views.create_student,name='create_student'),
    path('create_staff/', views.create_staff,name='create_staff'),
    path('update_student/<str:pk>', views.update_student,name='update_student'),
    # path('staff/', views.putprofile,name='create_staff'),
    path('update_staff/<str:pk>', views.update_staff,name='update_student'),
]