from django.contrib import admin

from django.contrib import admin
from .models import Category, Product, Supplier, PurchaseOrder, Sale, PurchaseOrderRequest, Brand

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'price', 'quantity', 'reorder_level')
    list_filter = ('category',)
    search_fields = ('name', 'category__name', 'brand__name')
    
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']

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

@admin.register(PurchaseOrderRequest)
class PurchaseOrderRequestAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'customer_email', 'customer_phone','description','created_at')
    list_filter = ('customer_name', 'customer_email', 'customer_phone',)
    search_fields = ('customer_name', 'customer_email', 'customer_phone')

