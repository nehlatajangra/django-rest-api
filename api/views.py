from django.http import JsonResponse
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render,HttpResponse
from rest_framework import viewsets,filters
from .models import Customer,Category,Product,Location,Apartment,Student,Employee,Interest
from .serializers import UModelSerializer,CModelSerializer,PModelSerializer,LoginModelSerializer,AppartmentSerializer,LocationSerializer,ApartmentFilter,StudentSerializer,EmployeeFilter,EmployeeSerializer
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
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ApartmentFilter
    filterset_fields=['house_name']
    
class StudentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    filter_backends=[DjangoFilterBackend,filters.SearchFilter]
    filterset_fields=['hobbies']
 
class EmployeeViewset(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class=EmployeeFilter
    
def password(request):
    return render(request,'password.html')
def ghar(request):
    return render(request, 'location.html')

def toastr(request):
    return render(request,'result.html')
    
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

def pop(request):
    catList=Category.objects.all()
    return render(request,"popup.html",{"category":catList})

def wordCounter(request):
    if request.method=='POST':
        print(request.method=='POST')
        data=request.POST.get('area1')
        space=0
        print(len(data))
        if data:
            words = data.split(' ')
            length = len(words)
            withSpace=len(data)
            for i in data:
                if i==' ':
                    space=length-1
            print(space)
            withoutSpace=withSpace-space
            print(withoutSpace)
        else:
            words = []
            length = 0
            withSpace=0
        context={
            'Words':words,
            'length':length,
            'withSpace':withSpace,
            'withoutSpace':withoutSpace
        }
        return render(request,"wordCounter.html",context)
    else:
        return render(request,"wordCounter.html")
    
def spinner(request):
    return render(request,'spinner.html')
        
# 33333333333333333333333333333333333333333
@api_view(['GET'])
def getUser(request):
    users = Customer.objects.all()
    serializer = UModelSerializer(users, many=True)
    return Response(serializer.data)

