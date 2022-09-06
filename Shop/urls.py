
from django.contrib import admin
from django.urls import path
from . import views

app_name='Shop'
urlpatterns = [
    path('home/',views.homeview,name='home'),
    path('product/<int:product_id>/',views.productview,name='product'),
    path('category/<str:category>/',views.categoryview,name='categories'),
    path('checkout/',views.checkoutview,name='checkout'),
    path('add_to_cart/<int:product_id>/',views.add_to_cart,name='add_to_cart'),
    path('remove_from_cart/<int:product_id>/',views.remove_from_cart,name='remove_from_cart'),
]
