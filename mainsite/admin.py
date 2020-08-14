from django.contrib import admin
from .models import Goods, Comment, Order, MainCatalog, Catalog, PropertyImage


class GoodsDb(admin.ModelAdmin):
    list_display = ('name', 'price', 'details', 'catalog', 'get_images')


class CommentDb(admin.ModelAdmin):
    list_display = ('text', 'goods', 'user')


class OrderDb(admin.ModelAdmin):
    list_display = ('user', 'date', 'get_goods', 'get_count_goods')


class CatalogDb(admin.ModelAdmin):
    list_display = ('name', 'mainCatalog')


admin.site.register(Goods, GoodsDb)
admin.site.register(Comment, CommentDb)
admin.site.register(Order, OrderDb)
admin.site.register(Catalog, CatalogDb)
admin.site.register(PropertyImage)
admin.site.register(MainCatalog)
