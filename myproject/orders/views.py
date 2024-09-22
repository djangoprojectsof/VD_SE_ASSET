from django.shortcuts import render
from .models import Order,Customer

def top_customers_view(request):
    top_customers = Order.top_customers()
    return render(request, 'orders/top_customers.html', {'top_customers': top_customers})
