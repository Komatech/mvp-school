from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(course)
admin.site.register(subject)
admin.site.register(fees)
admin.site.register(score)
admin.site.register(className)
admin.site.register(semester)