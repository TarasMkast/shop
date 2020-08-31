from django.contrib import admin
from .models import MainCatalog, Catalog


class CatalogDb(admin.ModelAdmin):
    list_display = ('name', 'mainCatalog')


admin.site.register(Catalog, CatalogDb)
admin.site.register(MainCatalog)
