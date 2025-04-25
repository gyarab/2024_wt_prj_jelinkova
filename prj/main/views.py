from django.shortcuts import render
from main.models import Product

def get_homepage(request):
    context = {
        "svatek": "Marek",
        # SELECT * from Product LIMIT 20;
        "products": Product.objects.all().order_by('name')[:2]
    }
    return render(request, "main/homepage.html", context)

def get_menu(request):
    context = {
        "svatek": "Marek",
        # SELECT * from Product LIMIT 20;
        "products": Product.objects.all().order_by('name')[:2]
    }
    return render(request, "main/menu.html", context)
