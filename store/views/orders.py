from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer
from django.views import View
from store.models.product import Products
from store.models.orders import Order
from store.middlewares.auth import auth_middleware



def orderView(request ):
    customer = request.session.get('customer')
    orderlist = Order.get_orders_by_customer(customer)
    print(orderlist)
    return render(request , 'orders.html'  , {'orders' : orderlist})
def deleteOrder(request,pk):
    """ Cancel an order from the profile page """
    order = Order.objects.get(id=pk)
    order.delete()
    return redirect('orders')
