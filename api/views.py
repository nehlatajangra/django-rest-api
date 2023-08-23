from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render,HttpResponse
from rest_framework import viewsets,filters
from .models import Customer,Category,Product
from .serializers import UModelSerializer,CModelSerializer,PModelSerializer
# Create your views here.
class CustomerViewset(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=UModelSerializer
    
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['first_name',"last_name","email"]
        
# class SelectedModelViewset(viewsets.ModelViewSet):
#     queryset=Customer.objects.all()
#     serializer_class=SelectedModelSerializer
    
#     filter_backends=[DjangoFilterBackend,filters.SearchFilter]
#     filterset_fields=['email']
    
    
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
        