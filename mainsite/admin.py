from django.contrib import admin
from .models import Goods, Comment, Order, MainCatalog, Catalog, PropertyImage


class GoodsDb(admin.ModelAdmin):
    list_display = ('name', 'price', 'details', 'catalog')


class CommentDb(admin.ModelAdmin):
    list_display = ('text', 'goods', 'user')


class OrderDb(admin.ModelAdmin):
    list_display = ('user', 'date', 'get_goods', 'get_count_goods')


class CatalogDb(admin.ModelAdmin):
    list_display = ('name', 'mainCatalog')


class Images(admin.ModelAdmin):
    list_display = ('image', 'goods')


admin.site.register(Goods, GoodsDb)
admin.site.register(Comment, CommentDb)
admin.site.register(Order, OrderDb)
admin.site.register(Catalog, CatalogDb)
admin.site.register(MainCatalog)
admin.site.register(PropertyImage, Images)
