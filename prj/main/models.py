from django.db import models

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
    product = models.ForeignKey('Product', null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey('User', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.content} ({self.product})"

class User(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.name}"