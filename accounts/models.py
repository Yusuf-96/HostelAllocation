from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

STATUS_CHOICES=[
    ('male','MALE'),
    ('female','FEMALE'),
]
# Create your models here.
class Profile(models.Model):
     user=models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
     status=models.CharField(max_length=10,choices=STATUS_CHOICES)
     phone=models.CharField(max_length=10,blank=True,null=True)
     location=models.CharField(max_length=100,blank=True,null=True)
     profile=models.ImageField(upload_to="images/users",blank=True,null=True,default='images/users/default/brand.png')
    

     def __str__(self):
         return f'{self.user}'

# @receiver(post_save, sender=User)
# def update_profile_signal(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#     instance.profile.save()