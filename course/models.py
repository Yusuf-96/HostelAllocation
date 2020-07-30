from django.db import models
from django.conf import settings
from department.models import Department
from django.urls import reverse
User=settings.AUTH_USER_MODEL

# Create your models here.
class Course(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='course')
   department=models.ForeignKey(Department,on_delete=models.CASCADE,related_name='course')
   name=models.CharField(max_length=100)


   def __str__(self):
      return self.name


   def remove_course(self):
      return reverse('course:delete',kwargs={'id':self.id})

