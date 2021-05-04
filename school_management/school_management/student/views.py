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
import hashlib

PASSWORD_SALT = "SaasSchoOlPoRtalHasH(8)!@4u*Q"

def hash_password(password):
    return hashlib.md5(PASSWORD_SALT + ((((hashlib.sha1(password.encode()).hexdigest()).encode()).hexdigest())))

# Create your views here.
def Signup(request):
    first_name = request.POST.get('first_name')
    password = request.POST.get('password')
    password = hash_password(password)
    
    studentProfile.objects.create(
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
    
    student = studentProfile.objects.filter(first_name=first_name, password = password)

    if student:
        # filter returns an array, only one record would be gotten using the above method
        student = student[0]
        print("Logged In")
    else:
        print("Login failed, please check your details")
    
    return render(request,'register.html')


# display student info
@api_view(['GET'])
def Profile(request):
    student = studentProfile.objects.all()
    serializer = studentSerializer(student,many=True)
    return Response(serializer.data)

# display all subjects offered
@api_view(['GET'])
def Subjects(request):
    sub = course.objects.filter(student__first_name=request.GET['first_name'])
    
    serializer = courseSerializer(sub,many=True)
    return Response(serializer.data)

# display continous assessment
@api_view(['GET'])
def assessment(request):
    assessment = score.objects.filter(name__student__first_name = request.GET['first_name'])

    serializer = scoreSerializer(assessment,many=True)
    data = serializer.data
    return Response({
        'messages': 'Result retrieved successfully',
        'status': True,
        'data' : data,
    },status=status.HTTP_200_OK)
    

# display result
@api_view(['GET'])
def result(request):
    term = semester.objects.all()
    results = []
    re = {}
    # print(result)
    # print(query)
    
    for a in term:
        result = score.objects.filter(name__student__first_name = request.GET['first_name'],name__semester=a)
        re['Semester'] = str(a)
        subjects_result = []
        sub = {}
        s=0

        for i in result:
            num = len(result)
            scores = i.totalScore
            sub['subject_name'] = str(i.name.subject)
            sub['subject_examScore'] = i.exam_score
            sub['subject_totalScore'] = scores
            sub['subject_grade'] = i.grade

            a = sub.copy()
            subjects_result.append(a)  

            try:
                s += i.totalScore
            except TypeError:
                return None

        re['result'] = subjects_result

        try:

            average = s/num
            re['average'] = average
            copy = re.copy()
            results.append(copy)

        except TypeError:
            return None
    # print(s)
    # print(average)
    # print(scores[0])
    
    # serializer = scoreSerializer(rio,many=True)
    # data = [serializer.data,{'average':average},{'score':subjectscore},{'grade':grades}]
    # data = {'average':average,'score':subjectscore,'grade':grades}
    return Response({
        'messages': 'Result retrieved successfully',
        'status': True,
        'data' : results,
    },status=status.HTTP_200_OK)
    # context = {
    #     'query':query,
    # }
    # return render(request,'index.html',context)


