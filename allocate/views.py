from django.shortcuts import render,redirect
from .models import Allocate
from django.db.models import F
from .models import Room
from django.views import View
from django.contrib import messages 
from .forms import AllocateForm
# Create your views here.


class Index(View):
    def get(self,*args,**kwargs):
        allocates=Allocate.objects.all()
        template_name='allocates/allocate_index.html'
        form=AllocateForm()
        context={
            'allocates':allocates,
            'form':form
        }
        return render(self.request,template_name,context)


    def post(self,*args,**kwargs):
        form=AllocateForm(self.request.POST or None)
        if form.is_valid():
            object=form.save(commit=False)
            object.user=self.request.user
            object.is_allocated=True
            object.save()
        messages.success(self.request,'allocate created successfully')
        return redirect('allocate:index')


class Update(View):
    def post(self,*args,**kwargs):
        id=kwargs['id']
        allocates=Allocate.objects.filter(id=id)
        form=AllocateForm(self.request.POST or None,instance=room)
        if form.is_valid():
            form.save()
        messages.success(self.request,'allocate updated successfully')
        return redirect('allocate:index')


def delete_allocate(request,id):
    allocate=Allocate.objects.filter(id=id)
    room_id=allocate[0].room.id
    room_level=allocate[0].room.level
    room_level-=1
    Room.objects.filter(id=room_id).update(level=room_level)
    allocate.delete()
    messages.success(request,'allocate deleted successfully')
    return redirect('allocate:index')



def approve_allocate(request,id):
    allocate=Allocate.objects.filter(id=id)
    allocate.update(is_approved=True)
    messages.success(request,f'You have approve {allocate[0].user} successfully')
    return redirect('allocate:index')

def undo_approve_allocate(request,id):
    allocate=Allocate.objects.filter(id=id)
    allocate.update(is_approved=False)
    messages.success(request,f'You have disqualified {allocate[0].user} successfully')
    return redirect('allocate:index')





