from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render,HttpResponse
from rest_framework import viewsets,filters
from .models import Customer,Category,Product,Location,Apartment
from .serializers import UModelSerializer,CModelSerializer,PModelSerializer,LoginModelSerializer,AppartmentSerializer,LocationSerializer
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from django.contrib.auth import authenticate, login

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
    filterset_fields = ["email","password"]
    
    
class CategoryViewset(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CModelSerializer
        
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ["cat_name"]
    
    
class ProductViewset(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=PModelSerializer
    
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['brand',"prod_name",]
    
class LocationViewset(viewsets.ModelViewSet):
    queryset=Location.objects.all()
    serializer_class=LocationSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['pincode','city']
    
class AppartmentViewset(viewsets.ModelViewSet):
    queryset=Apartment.objects.all()
    serializer_class=AppartmentSerializer
    
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['house_name','location']
    
def address(request):
    catList=Category.objects.all()
    return render(request,'address.html',{"category":catList})
    
def home(request):
    return render(request,'search.html')

def  catPage(request):
    return render(request,'catpage.html')

def addUser(request):
    return render(request,"userpage.html")

def addProduct(request):
    return render(request,"product.html")
        
    
def popUp(request):
    return render(request,'popUpForm.html')  

def wordCounter(request):
    # if request.method=='POST':
    #     data=request.POST.get('Textarea1','')
    #     print(data)
    #     if data:
    #         words = data.split(' ')
    #         length = len(words)
    #     else:
    #         words = []
    #         length = 0

    #     context={
    #         'Words':words,
    #         'length':length
    #     }
    #     return render(request,"wordCounter.html",context)
    return render(request,"wordCounter.html")  
        
# 33333333333333333333333333333333333333333
@api_view(['GET'])
def getUser(request):
    users = Customer.objects.all()
    serializer = UModelSerializer(users, many=True)
    return Response(serializer.data)

