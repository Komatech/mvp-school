from django.shortcuts import render,redirect
from .models import *
from Admin.models import *
from staff.models import *
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *


# Create your views here.

def get_average(average):
    print(average)
    return average.get('average')

@api_view(['GET'])
def best_student(request):
    
    student = studentProfile.objects.all()

    subjectscore = []
    grades = []
    average = []
    stu = {}
    for a in student:
        s=0
        result = score.objects.filter(name__student__first_name = a.first_name)
        stu['Name'] = a.first_name 
        # print(num)
        print(a)
        for i in result:
            print(i)
            num = len(result)
            scores = i.totalScore
            print(scores)
            subjectscore.append(scores)
            grade = i.grade
            grades.append(grade)
            s += scores
        
        try:
            print(num)
            averages = s/num
            stu['average'] = averages
            print(averages)
            status = stu.copy()
            average.append(status)
            # print(average)
        except TypeError:
            return None
        print(stu)
    best = average.sort(key=get_average,reverse=True)
    print(average)
    print(best)
    data = {'average':average}
    return Response({
        'messages': 'Result retrieved successfully',
        'status': True,
        'data' : data,
    },
    #  status=status.HTTP_200_OK
    )

@api_view(['GET'])
def total_students(request):
    students = studentProfile.objects.all()
    data = students.count()
    return Response({
        'messages': 'Result retrieved successfully',
        'status': True,
        'Total Students' : data,  
    }, status=status.HTTP_200_OK
    )

@api_view(['GET'])
def total_staff(request):
    roles = role.objects.all()
    staffs = {}
    role_names = []
    staff_total = staffProfile.objects.all().count()
    for i in roles:
        staff = staffProfile.objects.filter(role=i)
        print(i)
        staffs['Role'] = i.name
        # print(staff)
        data = staff.count()
        print(data)
        staffs["Number"] = data
        copy = staffs.copy()
        role_names.append(copy)
        
    print(role_names)

    return Response({
        'messages': 'Result retrieved successfully',
        'status': True,
        'Total Staff roles' : role_names,  
        'total staffs' : staff_total
    }, status=status.HTTP_200_OK
    )


def get_total(grades):
    # print(grades)
    # print(grades['scores'])
    return grades['scores']

@api_view(['GET'])
def best_student_subject(request):
    
    subjects = subject.objects.all()
    # print(course.objects.all())
    subjectscore = []
    
    stu = {}
    for a in subjects:
        stu['Subject Name'] = a.name
       
        cour = course.objects.filter(subject=a)
        result = score.objects.filter(name__subject = a)
        # print(result)
        grades = []
        cab = {}
        # for b in cour: 
        #     stu['Semester'] = b.semester.class_name.name + " " + b.semester.semester
                        
        for i in result:
            # print(i)
            
            stu['Semester'] = i.name.semester.class_name.name + " " + i.name.semester.semester
            num = len(result)
            cab['name'] = str(i.name.student)
            scores = i.totalScore
            cab['scores'] = scores

            se = cab.copy()
            grades.append(se)
        # print(grades.sort(key=get_total))
        
        stu['student'] = grades

        ab = stu.copy()
        subjectscore.append(ab)
    
        
        
    
        
    data = {'average':subjectscore}
    return Response({
        'messages': 'Result retrieved successfully',
        'status': True,
        'data' : data,
    },
    #  status=status.HTTP_200_OK
    )