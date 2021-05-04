from django.shortcuts import render,redirect
from .models import *
from student.models import *
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

# display staff info
@api_view(['GET'])
def staffprofile(request):
    staff = staffProfile.objects.all()
    serializer = staffSerializer(staff,many=True)
    return Response(serializer.data)

# display student info
@api_view(['GET'])
def studentprofile(request):
    student = studentProfile.objects.all()
    serializer = studentSerializer(student,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_student(request):
    serializer = studentSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def create_staff(request):
    serializer = staffSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        
    return Response(serializer.data)

@api_view(['PUT'])
def update_student(request,pk):
    student = studentProfile.objects.get(id=pk)
    
    serializer = studentSerializer(instance=student,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PUT'])
def update_staff(request,pk):
    staff = staffProfile.objects.get(id=pk)
    
    serializer = staffSerializer(instance=staff,data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)