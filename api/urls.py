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
# router.register('user',views.SelectedModelSerializer,basename='user')
urlpatterns = [
    path('search/',views.home,name='search'),
    path('catpage/',views.catPage,name='catpage'),
    path('adduser/',views.addUser,name="adduser"),
    path('addproduct/',views.addProduct,name="addProduct"),
    path('getUser/',views.getUser,name='getUser'),
    path('address/',views.address,name='address'),
    path('',views.popUp,name="popup")
]
urlpatterns+=router.urls