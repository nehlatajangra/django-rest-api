from rest_framework import serializers
from .models import Category,Product,Customer,Location,Apartment,Student,Employee,Interest
from rest_framework.validators import UniqueValidator
import django_filters
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=200)
    password = serializers.CharField(max_length=200)
            
            
# customer serializer 
class UModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=('id','email','password','first_name','last_name','address','age','phone_no','gender')       
        extra_kargs={
            "password":{'write_only':True}
        }  
        def create(self, validate_data):
            users=Customer.objects.create_user(validate_data["email"],
                                               password=validate_data["password"],
                                               first_name=validate_data["first_name"],
                                               last_name=validate_data["last_name"],
                                               address=validate_data["address"],
                                               age=validate_data["age"],
                                               phone_no=validate_data["phone_no"],
                                               gender=validate_data["gender"])
            return users
        
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

class ResetPasswordEmailSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
          
class LoginModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['id','email','password']
        
class CModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
        
class PModelSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    class Meta:
        model=Product
        fields='__all__'
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Location
        fields='__all__'
        
class AppartmentSerializer(serializers.ModelSerializer):
    location = LocationSerializer()
    class Meta:
        model=Apartment
        fields='__all__'
        
class ApartmentFilter(django_filters.FilterSet):
    city = django_filters.CharFilter(field_name='location__city', lookup_expr='exact')
    pincode = django_filters.NumberFilter(field_name='location__pincode', lookup_expr='exact')
    house_name=django_filters.CharFilter(field_name='house_name')

    class Meta:
        model = Apartment
        fields = []
        
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'
        
class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model=Interest
        fields='__all__'
        
class EmployeeSerializer(serializers.ModelSerializer):
    hobby=InterestSerializer()
    class Meta:
        model=Employee
        fields='__all__'
        
class EmployeeFilter(django_filters.FilterSet):
    hobbies=django_filters.CharFilter(field_name='hobby_name',lookup_expr='exact')
    class Meta:
        model = Employee
        fields = []
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        modal=get_user_model()
        fields=('id','username')