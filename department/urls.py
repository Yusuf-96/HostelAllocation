from django.urls import path
from .views import *


app_name='department'


urlpatterns=[
    path('',Index.as_view(),name='index'),
    path('update/<int:id>',Update.as_view(),name='update'),
    path('<int:id>',delete_department,name='delete'),
]