from django.contrib import admin
from django.urls import path
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import orderView,deleteOrder
from .middlewares.auth import  auth_middleware

admin.site.site_header = "Online-Store Admin"
admin.site.site_title = "Online-Store Admin Portal"
admin.site.index_title = "Online-Store Researcher Portal"

urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders',orderView, name='orders'),
    path('orders/<str:pk>/',deleteOrder, name='orderss'),


]
