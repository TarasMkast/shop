from django.contrib import admin
from .models import Contact


class ContactDb(admin.ModelAdmin):
    list_display = ('email', 'number_tel', 'address')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Contact, ContactDb)
