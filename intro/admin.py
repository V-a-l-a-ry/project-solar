from django.contrib import admin
from .models import Order, SolarProduct,SolarPanel
admin.site.register(SolarProduct)
admin.site.register(Order)
admin.site.register(SolarPanel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'panel_name', 'quantity', 'price', 'order_date', 'status')
    list_filter = ('status', 'order_date')
    search_fields = ('user__username', 'panel_name')
    ordering = ('-order_date',)
# Register your models here.
