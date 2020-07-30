from django.shortcuts import render,redirect
from .models import Course
from django.views import View
from django.contrib import messages 
from .forms import CourseForm
# Create your views here.


class Index(View):
    def get(self,*args,**kwargs):
        courses=Course.objects.all()
        template_name='courses/course_index.html'
        form=CourseForm()
        context={
            'courses':courses,
            'form':form
            
        }
        return render(self.request,template_name,context)


    def post(self,*args,**kwargs):
        form=CourseForm(self.request.POST or None)
        if form.is_valid():
            object=form.save(commit=False)
            object.user=self.request.user
            object.save()
            messages.success(self.request,'course created successfully')
        return redirect('course:index')


class Update(View):
    def post(self,*args,**kwargs):
        id=kwargs['id']
        course=Course.objects.filter(id=id)
        form=CourseForm(self.request.POST or None,instance=room)
        if form.is_valid():
            form.save()
        messages.success(self.request,'course updated successfully')
        return redirect('course:index')


def delete_course(request,id):
    course=Course.objects.filter(id=id)
    course.delete()
    return redirect('course:index')