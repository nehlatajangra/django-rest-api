from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render,HttpResponse
from rest_framework import viewsets,filters
from .models import Customer,Category,Product
from .serializers import UModelSerializer,CModelSerializer,PModelSerializer,LoginModelSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
# Create your views here.
class CustomerViewset(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=UModelSerializer
    
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['first_name',"last_name","email"]
    
class UserViewset(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=LoginModelSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["email"]
    
    
class CategoryViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CModelSerializer
        
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["cat_name","Customer"]
    
    
class ProductViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=PModelSerializer
    
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['brand',"prod_name",]
    
def home(request):
    return render(request,'search.html')

def  catPage(request):
    return render(request,'catpage.html')

def addUser(request):
    return render(request,"userpage.html")

def addProduct(request):
    return render(request,"product.html")
        
    
def popUp(request):
    return render(request,'popup.html')    
        
# 33333333333333333333333333333333333333333
@api_view(['GET'])
def getUser(request):
    users = Customer.objects.all()
    serializer = UModelSerializer(users, many=True)
    return Response(serializer.data)

