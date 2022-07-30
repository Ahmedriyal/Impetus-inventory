from django.contrib import admin

from .models import (
    Purchase_Detail,
    Inventory,
)


admin.site.register(Purchase_Detail)
admin.site.register(Inventory)
