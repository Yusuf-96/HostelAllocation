from django.shortcuts import render,redirect
from .models import Department
from django.views import View
from django.contrib import messages 
from .forms import DepartmentForm
# Create your views here.


class Index(View):
    def get(self,*args,**kwargs):
        departments=Department.objects.all()
        template_name='departments/department_index.html'
        form=DepartmentForm()
        context={
            'departments':departments,
            'form':form
        }
        return render(self.request,template_name,context)


    def post(self,*args,**kwargs):
        form=DepartmentForm(self.request.POST or None)
        if form.is_valid():
            form.save()
        messages.success(self.request,'department created successfully')
        return redirect('department:index')


class Update(View):
    def post(self,*args,**kwargs):
        id=kwargs['id']
        department=Department.objects.filter(id=id)[0]
        form=DepartmentForm(self.request.POST or None,instance=department)
        if form.is_valid():
            form.save()
        messages.success(self.request,'department updated successfully')
        return redirect('department:index')


def delete_department(request,id):
    department=Department.objects.filter(id=id)
    department.delete()
    messages.success(request,'department deleted successfully')
    return redirect('department:index')



