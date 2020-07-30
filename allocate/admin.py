from django.contrib import admin
from .models import Allocate
# Register your models here.
@admin.register(Allocate)
class AllocateAdmin(admin.ModelAdmin):
    list_display=[
        'user'
    ]