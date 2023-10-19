from django.urls import path
from . import views
from rest_framework  import routers



router=routers.DefaultRouter()
router.register('user',views.UserViewset,basename='user')
router.register('product',views.ProductViewset,basename='product')
router.register('category',views.CategoryViewset,basename='category')
router.register('location',views.LocationViewset,basename='location')
router.register('appartment',views.AppartmentViewset,basename='appartment')
router.register('student',views.StudentViewset,basename='student')
router.register('employee',views.EmployeeViewset,basename='employee')


urlpatterns = [
    path('search/',views.home,name='search'),
    path('Customer/',views.CustomerViewset.as_view(),name='Customer'),
    path('Login/',views.LoginApi.as_view(),name='login'),
    path('catpage/',views.catPage,name='catpage'),
    path('adduser/',views.addUser,name="adduser"),
    path('addproduct/',views.addProduct,name="addProduct"),
    path('getUser/',views.getUser,name='getUser'),
    path('address/',views.address,name='address'),
    path('',views.popUp,name="popup"),
    path('ajax/',views.ajaxDemo,name='ajex'),
    path('popup/',views.pop,name="pop"),
    path('counter/',views.wordCounter,name="wordCounter"),
    path('spinner/',views.spinner,name='spinner'),
    path('ghar/',views.ghar,name='ghar'),
    path('toastr/',views.toastr,name='toast'),
    path('test/',views.password,name='password'),
    path('change_password/',views.change_password, name='change_password'),
    path('gatData/',views.getUserData,name='get Data')

]
urlpatterns+=router.urls