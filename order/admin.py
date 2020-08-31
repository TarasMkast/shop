from django.contrib import admin

from order.models import Order, OrderProduct


class OrderProductDb(admin.ModelAdmin):
    list_display = ('order', 'product', 'price', 'quantity')


class OrderDb(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'address', 'city', 'created', 'paid')


admin.site.register(Order, OrderDb)
admin.site.register(OrderProduct, OrderProductDb)
