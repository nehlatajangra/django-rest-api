from rest_framework import serializers
from .models import Category,Product,Customer,Location,Apartment
from rest_framework.validators import UniqueValidator


class UModelSerializer(serializers.ModelSerializer):

    class Meta:
        model=Customer
        fields='__all__'
        
        
class LoginModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields=['id','email','password']
        
class CModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
        
class PModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'
        
class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Location
        fields='__all__'
        
class AppartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Apartment
        fields='__all__'