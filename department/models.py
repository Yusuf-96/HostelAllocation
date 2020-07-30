from django.db import models
from django.urls import reverse



# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
       return self.name
       
    def remove_department(self):
      return reverse('department:delete',kwargs={'id':self.id})

    def update_department(self):
      return reverse('department:update',kwargs={'id':self.id})
   
