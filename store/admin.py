from django.contrib import admin

from .models import (
    Category,
    Purchase_Detail,
    Inventory,
)

admin.site.register(Category)
admin.site.register(Purchase_Detail)
admin.site.register(Inventory)
