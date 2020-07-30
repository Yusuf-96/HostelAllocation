from django.urls import path
from .views import *


app_name='course'


urlpatterns=[
    path('',Index.as_view(),name='index'),
    path('update/<int:id>',Update.as_view(),name='update'),
    path('<int:id>',delete_course,name='delete'),
]