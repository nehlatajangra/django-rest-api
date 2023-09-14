from django.db import models

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
    
    
class Category(models.Model):
    cat_name=models.CharField(max_length=100,default="")
    
class Product(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE )
    prod_name=models.CharField(max_length=100,default="")
    brand=models.CharField(max_length=50,default="")
    price=models.IntegerField()
    desc=models.CharField(max_length=200,default="")
    
class Location(models.Model):
    pincode=models.IntegerField()
    city=models.CharField(max_length=50)
    
class Apartment(models.Model):
    house_number=models.IntegerField()
    house_name=models.CharField(max_length=100)
    floor=models.IntegerField()
    parking=models.BooleanField()
    location=models.ForeignKey(Location,on_delete=models.CASCADE, related_name='apartments_at_location')
