from django.db import models
from django.contrib.auth.models import User
from staff.models import *
from Admin.models import *
from management.models import *

# Create your models here.

class studentProfile(models.Model):
    institution_name = models.ForeignKey('management.institution',on_delete=models.CASCADE,null=True,blank=True)
    first_name = models.CharField(null=True,blank=True,max_length=50)
    middle_name = models.CharField(null=True,blank=True,max_length=50)
    last_name = models.CharField(null=True,blank=True,max_length=50)
    username = models.CharField(null=True,blank=True,max_length=50)
    password = models.CharField(null=True,blank=True,max_length=50)
    sex =  models.CharField(null=True,blank=True,max_length=50,choices=(('Male','Male'),('Female','Female')))
    dateOfBirth = models.DateField(auto_now=False,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    # classname = models.ForeignKey('Admin.currentClass',on_delete=models.CASCADE,null=True,blank=True)
    # image = models.ImageField()
    created_at = models.DateField(auto_now=True,null=True,blank=True)
    def __str__(self):
        return self.first_name




