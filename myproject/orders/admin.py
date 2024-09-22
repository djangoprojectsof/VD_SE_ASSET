from django.contrib import admin
from .models import Order,Customer
# Register your models here.
class OrderInline(admin.TabularInline):
    model = Order
    extra = 1  # Number of empty forms to display

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    inlines = [OrderInline]  # Show orders related to the customer

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'order_date', 'status', 'total_amount')
    list_filter = ('status', 'order_date')
    search_fields = ('customer__name',)