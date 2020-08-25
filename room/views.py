from django.shortcuts import render,redirect
from .models import Room
from allocate.models import Allocate
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.views import View
from django.contrib import messages 
from .forms import RoomForm
# Create your views here.


class Index(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required ='room.view_room'
    def get(self,*args,**kwargs):
        rooms=Room.objects.all()
        template_name='rooms/room_index.html'
        DefaultCapacity={
            'capacity':6,
            'name':'Room 100'
        }
        form=RoomForm(initial=DefaultCapacity)
        context={
            'rooms':rooms,
            'form' :form,
        }
        return render(self.request,template_name,context)

    def post(self,*args,**kwargs):
        form=RoomForm(self.request.POST or None)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=self.request.user
            instance.save()
            messages.success(self.request,'room created successfully')
        return redirect('room:index')


class Update(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'room.change_room'
    def post(self,*args,**kwargs):
        id_room=kwargs['id']
        room=Room.objects.filter(id=id_room)[0]
        form=RoomForm(self.request.POST or None,instance=room)
        if form.is_valid():
            form.save()
            messages.success(self.request,'room updated successfully')
            return redirect('room:index')
        else:
            print(form.errors)
            return redirect('room:index')

@login_required
@permission_required('room.delete_room')
def delete_room(request,id):
    room=Room.objects.filter(id=id)
    room.delete()
    messages.success(request,'room deleted successfully')
    return redirect('room:index')

class ApplyRoom(View):
    def get(self,*args,**kwargs):
        id=kwargs['id']
        room=Room.objects.filter(id=id)
        allocate=Allocate.objects.filter(
            room=room[0],
            user=self.request.user,
            is_allocated=True,

        )
        if not allocate.exists():
                nowlevel=room[0].level
                room.update(level=nowlevel+1)
                allocate=Allocate.objects.create(
                    room=room[0],
                    user=self.request.user,
                    is_allocated=True,
                )
                messages.success(self.request,f'Congrats! You have Apply for {room[0].name} successfully')
                return redirect('room:index')

        else:
            messages.warning(self.request,f'Soory! You have already Apply for {room[0].name} successfully')
            return redirect('room:index')

    



