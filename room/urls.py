from django.urls import path
from .views import *


app_name='room'


urlpatterns=[
    path('',Index.as_view(),name='index'),
    path('update/<int:id>/',Update.as_view(),name='update'),
    path('<int:id>/',delete_room,name='delete'),
    path('apply/<int:id>/',ApplyRoom.as_view(),name='apply'),
]