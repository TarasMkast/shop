from django.contrib import admin
from .models import Goods, Comment, Order, MainCatalog, Catalog, PropertyImage, OrderProduct


class GoodsDb(admin.ModelAdmin):
    list_display = ('name', 'price', 'details', 'catalog')


class CommentDb(admin.ModelAdmin):
    list_display = ('text', 'goods', 'user')


class OrderDb(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'address', 'city', 'created', 'paid')


class CatalogDb(admin.ModelAdmin):
    list_display = ('name', 'mainCatalog')


class Images(admin.ModelAdmin):
    list_display = ('image', 'goods')


class OrderProductDb(admin.ModelAdmin):
    list_display = ('order', 'goods', 'price', 'quantity')


admin.site.register(Goods, GoodsDb)
admin.site.register(Comment, CommentDb)
admin.site.register(Order, OrderDb)
admin.site.register(Catalog, CatalogDb)
admin.site.register(MainCatalog)
admin.site.register(PropertyImage, Images)
admin.site.register(OrderProduct, OrderProductDb)
