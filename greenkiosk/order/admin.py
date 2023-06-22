from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display  = ("order_status","items","customer_information","payment_details")
    
admin.site.register(Order,OrderAdmin) 

# Register your models here.
