from django.db import models
from department.models import Department
from course.models import Course
from django.conf import settings

User=settings.AUTH_USER_MODEL
GENDER_CHOICES=[
    ('male','MALE'),
    ('female','FEMALE'),
]

DISABILITY_CHOICES=[
    ('no','None'),
    ('yes','OTHERS'),
]
# Create your models here.
class Information(models.Model):
    user =  models.ForeignKey(User,on_delete=models.CASCADE,related_name='information')
    course =  models.ForeignKey(Course,on_delete=models.CASCADE,related_name='information')
    phone = models.CharField(max_length=20)
    department =  models.ForeignKey(Department,on_delete=models.CASCADE,related_name='information')
    gender     =  models.CharField(max_length=10,choices=GENDER_CHOICES)
    disability =  models.CharField(max_length=50,choices=DISABILITY_CHOICES)

    def __str__(self):
        return f'{self.course}'
