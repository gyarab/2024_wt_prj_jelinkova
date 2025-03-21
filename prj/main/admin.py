from django.contrib import admin
from .models import Product
from .models import Category

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "category"]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
