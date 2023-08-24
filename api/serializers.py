from rest_framework import serializers
from .models import Category,Product,Customer

class UModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'
        

        
class CModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
        
class PModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields='__all__'