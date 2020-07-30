from django.shortcuts import render,redirect
from .models import Hostel
from django.views import View
from .forms import HostelForm
from django.contrib import messages 
# Create your views here.

class Index(View):
    def get(self,*args,**kwargs):
        hostels=Hostel.objects.all()
        template_name='hostels/hostel_index.html'
        form=HostelForm()
        context={
            'hostels':hostels,
            'form':form,
        }
        return render(self.request,template_name,context)


    def post(self,*args,**kwargs):
        hostels=Hostel.objects.all()
        form=HostelForm(self.request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(self.request,'hostel created successfully')
        return redirect('hostel:index')


class Update(View):
    def post(self,*args,**kwargs):
        id=kwargs['id']
        hostel=Hostel.objects.filter(id=id)[0]
        form=HostelForm(self.request.POST or None,instance=hostel)
        if form.is_valid():
            form.save()
            messages.success(self.request,'hostel updated successfully')
        return redirect('hostel:index')


def delete_hostel(request,id):
    hostel=Hostel.objects.filter(id=id)
    hostel.delete()
    messages.success(request,'hostel deleted successfully')
    return redirect('hostel:index')
