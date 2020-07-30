from django.contrib import admin
from .models import Department
admin.site.site_header = "HAMS ADMINISTRATION"
# Register your models here.
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display=[
        'name'
    ]