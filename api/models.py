from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class  Customer(models.Model):
    email=models.EmailField()
    password=models.CharField(max_length=8,blank=False,default="admin123")
    first_name=models.CharField(max_length=50 ,default="")
    last_name=models.CharField(max_length=50,default="")
    address=models.CharField(max_length=100,default="")
    age=models.IntegerField()
    phone_no=models.CharField(max_length=12,default="")
    gender_choice=(('Male','M'),('Female','F'))
    gender=models.CharField(max_length=10,choices=gender_choice,default="")
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
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

    
