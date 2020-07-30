from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from allocate.models import Allocate

# Create your views here.
class Home(LoginRequiredMixin,View):
    def get(self,*args,**kwargs):
        allocates=Allocate.objects.filter(user=self.request.user)
        context={
            'allocates':allocates
        }
        template_name='home.html'
        return  render(self.request,template_name,context)

class Admin(LoginRequiredMixin,View):
    def get(self,*args,**kwargs):
        template_name='admin.html'
        return  render(self.request,template_name)

