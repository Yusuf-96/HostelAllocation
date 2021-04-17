from django.contrib import admin

from .models import Hostel
# Register your models here.
@admin.register(Hostel)
class HostelAdmin(admin.ModelAdmin):
    list_display=[
        'name', 'category'
    ]