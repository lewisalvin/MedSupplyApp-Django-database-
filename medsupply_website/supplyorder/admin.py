from django.contrib import admin
from .models import Customer
from .models import Orders
from .models import Products
from .models import OrderDetails

#admin.site.register(Customer)
admin.site.register(Orders)
admin.site.register(Products)
admin.site.register(OrderDetails)

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'insurance', 'address')
    ordering = ('lastName',)
    search_fields = ('firstName', 'lastName', 'address')

