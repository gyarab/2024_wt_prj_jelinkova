from django.contrib import admin
from .models import Product
from .models import Category
from .models import Review
from .models import User
from .models import Diet
from .models import ProductDiet

class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "category"]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class ReviewAdmin(admin.ModelAdmin):
    list_display = ["id", "content", "product", "user", "stars"]

class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class DietAdmin(admin.ModelAdmin):
    list_display = ["id", "name"]

class ProductDietAdmin(admin.ModelAdmin):
    list_display = ["id", "product", "diet"]

# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Diet, DietAdmin)
admin.site.register(ProductDiet, ProductDietAdmin)
