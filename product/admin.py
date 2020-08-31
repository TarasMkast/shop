from django.contrib import admin
from .models import Product, PropertyImage


class ProductDb(admin.ModelAdmin):
    list_display = ('name', 'price', 'details', 'catalog')


class Images(admin.ModelAdmin):
    list_display = ('image', 'product')


admin.site.register(Product, ProductDb)
admin.site.register(PropertyImage, Images)
