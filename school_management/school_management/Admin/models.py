from django.db import models
from student.models import *
from staff.models import *
from management.models import *

# Create your models here.
class course(models.Model):
    # name = models.CharField(null=True,blank=True,max_length=50)
    student = models.ForeignKey('student.studentProfile',related_name='student_course',on_delete=models.CASCADE,null=True,blank=True)
    status = models.CharField(null=True,blank=True,max_length=50,choices=(('Active','Active'),('Inactive','Inactive')))
    # school_fees = models.ForeignKey('fees',on_delete=models.CASCADE,null=True,blank=True)
    subject = models.ForeignKey('subject',on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateField(auto_now=True)
    semester = models.ForeignKey('semester',on_delete=models.CASCADE,null=True,blank=True)
    institution_name = models.ForeignKey('management.institution',on_delete=models.CASCADE,null=True,blank=True)
    

    def __str__(self):
        return str(self.semester) + ' for ' + str(self.student) + ' in ' +str(self.subject)

class subject(models.Model):
    name = models.CharField(null=True,blank=True,max_length=50)
    created_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class semester(models.Model):
    institution_name = models.ForeignKey('management.institution',on_delete=models.CASCADE,null=True,blank=True)
    class_name = models.ForeignKey('className',on_delete=models.CASCADE,null=True,blank=True)
    semester = models.CharField(null=True,blank=True,max_length=50,choices=(('First Semester','First Semester'),('Second Semester','Second Semester'),('Third Semester','Third Semester')))
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return str(self.class_name) + " " + self.semester

class score(models.Model):
    name = models.ForeignKey(course,related_name='course_score',on_delete=models.CASCADE,null=True,blank=True)
    attendance_score = models.FloatField(null=True,blank=True)
    test_score = models.FloatField(null=True,blank=True)
    exam_score = models.FloatField(null=True,blank=True)
    status = models.CharField(null=True,blank=True,max_length=50,choices=(('Active','Active'),('Inactive','Inactive')))
    created_at = models.DateField(auto_now=True)
    institution_name = models.ForeignKey('management.institution',on_delete=models.CASCADE,null=True,blank=True)
    # student = models.ForeignKey('student.studentProfile',related_name='student_score',on_delete=models.CASCADE,null=True,blank=True)
    staff = models.ForeignKey('staff.staffProfile',on_delete=models.CASCADE,null=True,blank=True)

    @property
    def contAsses(self):
        try:
            return self.attendance_score + self.test_score
        except TypeError:
            return None

    @property
    def totalScore(self):
        try:
            return self.exam_score + self.attendance_score + self.test_score
        except TypeError:
            return None

    @property
    def grade(self):
        try:
            if self.totalScore < 50:
                return 'F'

            if self.totalScore >= 50 and self.totalScore < 60 :
                return 'C'

            if self.totalScore >= 60 and self.totalScore < 70 :
                return 'B'

            if self.totalScore >= 70 :
                return 'A'
        except TypeError:
            return None

    # @property
    # def average(self):
    #     try: 
    #         sum1=0
    #         for i in self.totalScore:
    #             sum1 += i
    #         av1 = sum1 / len(self.totalScore)
    #         return av1
    #     except TypeError:
    #         return None

    def __str__(self):
        # return self.name.name
        return str(self.name)


class fees(models.Model):
    institution_name = models.ForeignKey('management.institution',on_delete=models.CASCADE,null=True,blank=True)
    class_name = models.CharField(null=True,blank=True,max_length=50)
    amount_due = models.FloatField(null=True,blank=True)
    amount_payed = models.FloatField(null=True,blank=True)
    
    @property
    def amountOwed(self):
        return self.amount_due - self.amount_payed

    @property
    def percentagePaid(self):
        fraction = self.amount_payed / (self.amount_due + self.amount_payed)
        percentage = fraction * 100
        return percentage

class className(models.Model):
    institution_name = models.ForeignKey('management.institution',on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(null=True,blank=True,max_length=50)
    created_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.name