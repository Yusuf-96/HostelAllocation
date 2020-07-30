from django.urls import path
from .views import *

urlpatterns=[
    path('',Home.as_view(),name='home'),
    path('',Admin.as_view(),name='admin_dashboard'),
]