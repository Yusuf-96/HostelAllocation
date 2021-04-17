from django.contrib import admin
from .models import Information
# Register your models here.
@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display=[
        'user'
    ]