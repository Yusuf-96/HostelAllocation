from django.urls import path
from .views import *


app_name='allocate'


urlpatterns=[
    path('',Index.as_view(),name='index'),
    path('update/<int:id>',Update.as_view(),name='update'),
    path('<int:id>',delete_allocate,name='delete'),
]