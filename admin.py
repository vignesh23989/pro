from django.contrib import admin

# Register your models here.
from .models import Department, Student

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]

class StudentAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name", "phone", "gender", "address"]
    # To access django models with shell


admin.site.register(Student, StudentAdmin)
admin.site.register(Department, DepartmentAdmin)