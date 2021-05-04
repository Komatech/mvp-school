from rest_framework import serializers
from .models import *
from Admin.models import *
from staff.models import *

class studentSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentProfile
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'sex',
            'dateOfBirth',
            'age',
        ]

class scoreSerializer(serializers.ModelSerializer):
    subject_name = serializers.CharField(source='name',read_only=True)
    class Meta:
        model = score
        fields = [
            'subject_name',
            'attendance_score',
            'test_score',
            'exam_score',
            'status',
        ]

class courseSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student',read_only=True)
    subject_name = serializers.CharField(source='subject',read_only=True)
    semester_name = serializers.CharField(source='semester',read_only=True)

    class Meta:
        model = course
        fields = [
            'student_name',
            'status',
            'subject_name',
            'semester_name',
        ]