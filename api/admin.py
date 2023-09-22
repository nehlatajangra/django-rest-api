from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .models import Category,Product,Customer,Apartment,Location,Student,Employee,Interest

        
class StudentAdmin(admin.ModelAdmin):
    list_display=['student_name','student_class','hobbies']
    
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['emp_name','emp_role','interest']

    
    
# Register your models here.
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Location)
admin.site.register(Apartment)
admin.site.register(Student, StudentAdmin)
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Interest)


