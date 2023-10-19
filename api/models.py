from django.db import models
from django.utils.safestring import mark_safe
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager,AbstractBaseUser
from django.contrib.auth.models import AbstractUser

# class UserManager(BaseUserManager):
#     def create_user( self, email, password=None, is_staff=False, is_active=True, is_superuser=False, **extra_fields ):
#         """Create a user instance with the given email and password."""
#         email = UserManager.normalize_email(email)
#         extra_fields.pop("username", None)
#         user = self.model(email=email, is_active=is_active, is_staff=is_staff, is_superuser=is_superuser ,**extra_fields)
#         if password:
#             user.set_password(password)
#         user.save()
#         return user
                
#     def create_superuser(self, email, password=None, **extra_fields):
#         return self.create_user( email, password, is_staff=True, is_superuser=True, **extra_fields )    
# Create your models here.

class Customer(models.Model):
    email=models.EmailField()
    first_name=models.CharField(max_length=50 ,default="")
    last_name=models.CharField(max_length=50,default="")
    address=models.CharField(max_length=100,default="")
    age=models.IntegerField()
    phone_no=models.CharField(max_length=12,default="")
    gender_choice=(('Male','M'),('Female','F'))
    gender=models.CharField(max_length=10,choices=gender_choice,default="")
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
# class CustomUser(AbstractUser):
#     email = models.EmailField(unique=True )

#     def __str__(self):
#         return self.username
    
class Category(models.Model):
    cat_name=models.CharField(max_length=100,default="")
    def __str__(self):
        return f"{self.cat_name}"
    
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE )
    prod_name=models.CharField(max_length=100,default="")
    brand=models.CharField(max_length=50,default="")
    price=models.IntegerField()
    desc=models.CharField(max_length=200,default="")
    def __str__(self):
        return f"{self.prod_name}"
    
class Location(models.Model):
    pincode=models.IntegerField()
    city=models.CharField(max_length=50)
    
class Apartment(models.Model):
    house_number=models.IntegerField()
    house_name=models.CharField(max_length=100)
    floor=models.IntegerField()
    parking=models.BooleanField()
    location=models.ForeignKey(Location,on_delete=models.CASCADE,related_name="laction_apartment")
    def __str__(self):
        return f"{self.house_name}"
    
class Interest(models.Model):
    hobby_name=models.CharField(max_length=20)
    def __str__(self):
        return f"{self.hobby_name}"
    
class Employee(models.Model):
    emp_name=models.CharField(max_length=10)
    emp_role=models.CharField(max_length=200)
    hobby=models.ManyToManyField(Interest)
    def __str__(self):
        return f"{self.emp_name}"
    def interest(self):
        hob = [str(i) for i in self.hobby.all()]
        return mark_safe("<br>".join(hob))
    
    
class Student(models.Model):
    student_name=models.CharField(max_length=20)
    student_class=models.CharField(max_length=20)
    hobbies=models.TextField(max_length=20)

    def __str__(self):
        return self.hobbies

    def save(self, *args, **kwargs):
        # Split the text_field value by commas and join with newline
        if self.hobbies:
            values = self.hobbies.split(',')
            self.hobbies = '\n'.join(map(str.strip, values))
        super(Student, self).save(*args, **kwargs)

    
