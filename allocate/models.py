from django.db import models
from django.conf import settings
from room.models import Room
from django.urls import reverse
User=settings.AUTH_USER_MODEL
# Create your models here.
class Allocate(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='allocate')
    room = models.ForeignKey(Room, on_delete=models.CASCADE,related_name='allocate')
    is_allocated = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.user}' 

    def remove_allocate(self):
          return reverse('allocate:delete',kwargs={'id':self.id})

    def approve_allocate(self):
          return reverse('allocate:approve',kwargs={'id':self.id})

    def undo_approve(self):
      return reverse('allocate:undo_approve',kwargs={'id':self.id})

    def update_allocate(self):
      return reverse('allocate:update',kwargs={'id':self.id})
