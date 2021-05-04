from django.db import models
from student.models import *
from Admin.models import *
from management.models import *
# Create your models here.

class staffProfile(models.Model):
    institution_name = models.ForeignKey('management.institution',on_delete=models.CASCADE,null=True,blank=True)
    first_name = models.CharField(null=True,blank=True,max_length=50)
    middle_name = models.CharField(null=True,blank=True,max_length=50)
    last_name = models.CharField(null=True,blank=True,max_length=50)
    dateOfBirth = models.DateField(auto_now=False,null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    role = models.ForeignKey('role',on_delete=models.CASCADE,null=True,blank=True)
    # subject_handled = models.ManyToManyField(subject,null=True,blank=True)
    leaves = models.IntegerField(null=True,blank=True)
    paycheck = models.IntegerField(null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    sex =  models.CharField(null=True,blank=True,max_length=50,choices=(('Male','Male'),('Female','Female')))
    
    # image = models.ImageField()

    def __str__(self):
        return self.first_name

class role(models.Model):
    institution_name = models.ForeignKey('management.institution',on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(null=True,blank=True,max_length=50)

    def __str__(self):
        return self.name