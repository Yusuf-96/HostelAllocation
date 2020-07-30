from django.db import models
from django.urls import reverse
CATEGORY_CHOICE=[  
    ('male','Male'),
    ('female','female'),
]
# Create your models here.
class Hostel(models.Model):
    name=models.CharField(max_length=100)
    category=models.CharField(choices=CATEGORY_CHOICE,max_length=10)


    def __str__(self):
       return self.name

    def remove_hostel(self):
      return reverse('hostel:delete',kwargs={'id':self.id})
    def update_hostel(self):
      return reverse('hostel:update',kwargs={'id':self.id})
