from django.contrib import admin
from .models import Catalog


class CatalogDb(admin.ModelAdmin):
    list_display = ('name', 'parent_id')


admin.site.register(Catalog, CatalogDb)

