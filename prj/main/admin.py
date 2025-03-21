from django.contrib import admin
from .models import Product
from .models import Category
from .models import Review

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "category"]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "content", "product"]

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
