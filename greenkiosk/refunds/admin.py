from django.contrib import admin

from .models import Refunds

# Register your models here.
class RefundsAdmin(admin.ModelAdmin):
    list_display  = ("orderId","refundsId","amount","reason","requestDate","processDate")
    
admin.site.register(Refunds, RefundsAdmin) 
