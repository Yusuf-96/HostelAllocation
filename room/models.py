from django.db import models
from department.models import Department
from django.conf import settings
from django.urls import reverse

from hostel.models import Hostel
User=settings.AUTH_USER_MODEL
# Create your models here.
class Room(models.Model):
   user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='room')
   hostel=models.ForeignKey(Hostel,on_delete=models.CASCADE,related_name='room')
   name=models.CharField(max_length=100)
   is_taken=models.BooleanField(default=False)
   capacity=models.IntegerField()
   level=models.IntegerField(default=0)


   def __str__(self):
      return self.name


   def remove_room(self):
      return reverse('room:delete',kwargs={'id':self.id})

   def update_room(self):
      return reverse('room:update',kwargs={'id':self.id})


   def apply_room(self):
      return reverse('room:apply',kwargs={'id':self.id})