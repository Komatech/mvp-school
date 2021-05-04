from rest_framework import serializers
from .models import *
from student.models import *
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

class staffSerializer(serializers.ModelSerializer):
    class Meta:
        model = staffProfile
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'sex',
            'dateOfBirth',
            'age',
            'role',
            'leaves',
            'paycheck',
        ]

class roleSerializer(serializers.ModelSerializer):
    class Meta:
        model = role
        fields = [
            'name',
        ]

class scoreSerializer(serializers.ModelSerializer):
    # subject_name = serializers.CharField(source='name')
    # staff_name = serializers.CharField(source='staff')
    class Meta:
        model = score
        fields = [
            'name',
            # 'subject_name',
            'attendance_score',
            'test_score',
            'exam_score',
            'status',
            # 'staff_name',
            'staff',
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