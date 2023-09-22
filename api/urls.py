from django.urls import path
from . import views
from rest_framework  import routers



router=routers.DefaultRouter()
router.register('Customer',views.CustomerViewset,basename='Customer')
router.register('user',views.UserViewset,basename='user')
router.register('product',views.ProductViewset,basename='product')
router.register('category',views.CategoryViewset,basename='category')
router.register('location',views.LocationViewset,basename='location')
router.register('appartment',views.AppartmentViewset,basename='appartment')
router.register('student',views.StudentViewset,basename='student')
router.register('employee',views.EmployeeViewset,basename='employee')
urlpatterns = [
    path('search/',views.home,name='search'),
    path('catpage/',views.catPage,name='catpage'),
    path('adduser/',views.addUser,name="adduser"),
    path('addproduct/',views.addProduct,name="addProduct"),
    path('getUser/',views.getUser,name='getUser'),
    path('address/',views.address,name='address'),
    path('',views.popUp,name="popup"),
path('popup/',views.pop,name="pop"),
    path('counter/',views.wordCounter,name="wordCounter"),
    path('spinner/',views.spinner,name='spinner'),
    path('ghar/',views.ghar,name='ghar'),
    path('toastr/',views.toastr,name='toast'),
    path('test/',views.password,name='password')
]
urlpatterns+=router.urls