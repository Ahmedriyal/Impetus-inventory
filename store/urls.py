from django.urls import path

from .views import (
    category,
    Purchase,
    create_inventory,
    CategoryListView,
    PurchaseListView,
    InventoryListView,
    inventory_delete,
    inventory_edit,
    pdf_report_create,
    purchase_pdf_create
)

urlpatterns = [
    path('category/', category, name='category'),
    path('purchase-detail/', Purchase, name='purchase-detail'),
    path('create-inventory/', create_inventory, name='create-inventory'),
    path('category-list/', CategoryListView, name='category-list'),
    path('purchase-list/', PurchaseListView, name='purchase-list'),
    path('inventory-list/', InventoryListView, name='inventory-list'),
    path('inventory-list/delete/<int:pk>/', inventory_delete,
         name='inventory-item-delete'),
    path('inventory-list/edit/<int:pk>/', inventory_edit,
         name='inventory-item-edit'),
    path('create-pdf', pdf_report_create, name='create-pdf'),
    path('purchase-pdf', purchase_pdf_create, name='purchase-pdf'),
]
