from django.shortcuts import render,redirect
from .models import *
from Admin.models import *
from staff.models import *
# from django.contrib.auth import authenticate,login,logout,get_user_model
# from django.contrib.auth.models import Group
from django.contrib import messages
# from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
import hashlib

# Create your views here.
PASSWORD_SALT = "SaasSchoOlPoRtalHasH(8)!@4u*Q"

def hash_password(password):
    return hashlib.md5(PASSWORD_SALT + ((((hashlib.sha1(password.encode()).hexdigest()).encode()).hexdigest())))

def Signup(request):
    first_name = request.POST.get('first_name')
    password = request.POST.get('password')
    password = hash_password(password)
    
    staffProfile.objects.create(
        first_name=first_name,
        password = password
    )

    print(first_name)
    print(request.POST)
    return render(request,'register.html')

def Login(request):
    # not tested but this is th way
    first_name = request.POST.get('first_name')
    password = request.POST.get('password')
    password = hash_password(password)
    
    staff = staffProfile.objects.filter(first_name=first_name, password = password)

    if student:
        # filter returns an array, only one record would be gotten using the above method
        student = student[0]
        print("Logged In")
    else:
        print("Login failed, please check your details")
    
    return render(request,'register.html')
# display staff info
@api_view(['GET'])
def profile(request):
    staff = staffProfile.objects.filter(first_name=request.GET['first_name'])
    serializer = staffSerializer(staff,many=True)
    data = serializer.data
    return Response({
        'messages': 'Result retrieved successfully',
        'status': True,
        'data' : data,
    },status=status.HTTP_200_OK)

@api_view(['GET'])
def display_students(request):
    students = course.objects.filter(subject__name = 'English').filter(semester__class_name__name='SS1 A')
    serializer = courseSerializer(students,many=True)
    data = serializer.data
    return Response({
        'messages': 'Result retrieved successfully',
        'status': True,
        'data' : data,
    },status=status.HTTP_200_OK)

@api_view(['GET'])
def view_scores(request):
    scores = score.objects.filter(name__subject__name = 'English')
    serializer = scoreSerializer(scores,many=True)
    data = serializer.data
    return Response({
        'messages': 'Result retrieved successfully',
        'status': True,
        'data' : data,
    },status=status.HTTP_200_OK)

@api_view(['GET'])
def view_student_score(request,pk):
    scores = score.objects.filter(name__subject__name = 'English').get(id=pk)
    serializer = scoreSerializer(scores,many=False)
    data = serializer.data
    return Response({
        'messages': 'Result retrieved successfully',
        'status': True,
        'data' : data,
    },status=status.HTTP_200_OK)

@api_view(['POST'])
def upload_scores(request):
    serializer = scoreSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    data = serializer.data
    return Response({
        'messages': 'Result retrieved successfully',
        'status': True,
        'data' : data,
    },status=status.HTTP_200_OK)


@api_view(['POST'])
def putprofile(request):
    serializer = staffSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        
    data = serializer.data
    return Response({
        'messages': 'Result retrieved successfully',
        'status': True,
        'data' : data,
    },status=status.HTTP_200_OK)

@api_view(['PUT'])
def update_student_score(request,pk):
    scores = score.objects.filter(name__subject__name = 'English').get(id=pk)
    
    serializer = scoreSerializer(instance=scores,data=request.data)

    if serializer.is_valid():
        serializer.save()

    data = serializer.data
    return Response({
        'messages': 'Result retrieved successfully',
        'status': True,
        'data' : data,
    },status=status.HTTP_200_OK)