from datetime import datetime
import json
import time
from django.conf import settings
from django.http import JsonResponse
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets,filters,status,generics
from .models import Customer,Category,Product,Location,Apartment,Student,Employee,Interest
from .serializers import *
from rest_framework.decorators import api_view
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, login
from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password,make_password

class LoginApi(generics.GenericAPIView):
    serializer_class = LoginSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data
        email = data['email']
        password = data['password']
        user = Customer.objects.get(email = email)
        validate = check_password(password, user.password)
        print(validate)
        
        if validate:
            token = str(RefreshToken.for_user(user))
            access = str(RefreshToken.for_user(user).access_token)
            return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "access": access,
            "refresh": token,

            })
        else:
            content = {"detail": "Password Do not Match"}
            return Response(content, status=status.HTTP_404_NOT_FOUND)

        content = {"detail": "No active account found with the given credentials"}
        return Response(content, status=status.HTTP_404_NOT_FOUND)
        
                
# Create your views here.
class CustomerViewset(generics.CreateAPIView):
    queryset=Customer.objects.all()
    permission_classes=(AllowAny,)
    serializer_class=UModelSerializer
    
    def create(self, request, *args, **kwargs):
        response=super(CustomerViewset,self).create(request,*args,**kwargs)
        if response.status_code==201:
            user=Customer.objects.get(pk=response.data['id'])
            token=str(RefreshToken.for_user(user))
            access=str(RefreshToken.for_user(user).access_token)

            # Calculate the expiration time of the access token
            expiration_time = datetime.now() + settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"]

            return Response({
                "user":UModelSerializer(user,context=self.get_serializer_context()).data,
                "access":access,
                "refresh":token,
                "expiration_time":expiration_time.timestamp()
            },
            status=status.HTTP_201_CREATED)
        print(response)
        return response    
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filterset_fields = ['first_name',"last_name","email"]
    

    
def getUserData(request):
    if request.method == "POST":
        try:
            data = json.loads(request.POST.get('userData'))
            userToken = data.get('access')
            print(userToken)
        except json.JSONDecodeError:
            return HttpResponse("Invalid JSON data", status=400)

    response_text = "This is a response from my view."
    return HttpResponse(response_text)


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

def ajaxDemo(request):
    return render(request,"Ajax.html")
    
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


class UserAPIView(RetrieveAPIView):
    permission_classes=(IsAuthenticated)
    serializer_class=UserSerializer
    
    def get_object(self):
        return self.request.user
    
    
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import update_session_auth_hash
from .serializers import ChangePasswordSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password(request):
    if request.method == 'POST':
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            if user.check_password(serializer.data.get('old_password')):
                user.set_password(serializer.data.get('new_password'))
                user.save()
                update_session_auth_hash(request, user)  # To update session after password change
                return Response({'message': 'Password changed successfully.'}, status=status.HTTP_200_OK)
            return Response({'error': 'Incorrect old password.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)