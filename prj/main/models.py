from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.name} ({self.price})"
    
class Category(models.Model):
    name = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.name}"
    
class Review(models.Model):
    content = models.TextField(max_length=400)
    product = models.ForeignKey('Product', null=True, on_delete=models.CASCADE)
    user = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)
    stars = models.IntegerField(
    null=True,
    validators=[
        MinValueValidator(1),
        MaxValueValidator(5),
    ]
)

    def __str__(self):
        return f"{self.content} ({self.stars})"

class User(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name}"
    
class Diet(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name}"
    
class ProductDiet(models.Model):
    product = models.ForeignKey('Product', null=True, on_delete=models.CASCADE)
    diet = models.ForeignKey('Diet', null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.product}  ({self.diet})"