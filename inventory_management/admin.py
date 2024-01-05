from django.contrib import admin

from django.contrib import admin
from .models import Category, Product, Supplier, PurchaseOrder, Sale

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'reorder_level')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'email', 'phone')
    search_fields = ('name', 'contact_person', 'email', 'phone')

@admin.register(PurchaseOrder)
class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'supplier', 'quantity', 'order_date', 'delivery_date', 'received')
    list_filter = ('supplier', 'received')
    search_fields = ('product__name', 'supplier__name')

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity_sold', 'sale_date')
    list_filter = ('product',)
    search_fields = ('product__name',)

