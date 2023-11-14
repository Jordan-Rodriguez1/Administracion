from django.contrib import admin
from .models import address

class AddressAdmin(admin.ModelAdmin):
    readonly_fields = ("created", "is_default")

# Register your models here.
admin.site.register(address, AddressAdmin)
