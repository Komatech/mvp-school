from django.db import models

# Create your models here.

class institution(models.Model):
    name = models.CharField(null=True,blank=True,max_length=250)
    created_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name