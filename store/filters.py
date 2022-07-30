import django_filters
from django_filters import CharFilter

from .models import *

class PurchaseFilter(django_filters.FilterSet):
    class Meta:
        model = Purchase_Detail
        fields = ['category', 'purchased_by']


class InventoryFilter(django_filters.FilterSet):
    device_name = CharFilter(field_name='device_name', lookup_expr='icontains')
    
    class Meta:
        model = Inventory
        fields = ['category', 'device_name']