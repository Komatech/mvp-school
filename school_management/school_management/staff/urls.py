from django.contrib import admin
from django.urls import path
from staff import views


urlpatterns = [
    path('', views.profile,name='staff_home'),
    path('students/', views.display_students,name='studentslist'),
    path('scores/', views.view_scores,name='view_student_scores'),
    path('scores/<str:pk>', views.view_student_score,name='view_student_score'),
    path('upload/', views.upload_scores,name='score_upload'),
    path('staff/', views.putprofile,name='create_staff'),
    path('Update/<str:pk>', views.update_student_score,name='update_student_score'),
]