from django.urls import path,include
from . import views

urlpatterns = [

    path('',views.home,name="home"),
    path('category/<int:categoryid>/',views.Category,name="Category"),
    path('product/<int:productid>/',views.Product,name="Product"),
    path('newproducts/',views.newproducts,name="newproducts"),
    path('add/<int:productid>/',views.add,name="add"),
    path('cart/',views.carti,name="carti"),
]
