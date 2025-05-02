from django.shortcuts import render
from main.models import Product

def get_homepage(request):
    products = Product.objects.all().order_by('name')
    # filter by title if query parameter search is present
    search = request.GET.get('search')
    if search:
        products = products.filter(name__icontains=search)
        
    context = {
        "svatek": "Marek",
        # SELECT * from Product LIMIT 20;
        "products": products
    }
    return render(request, "main/homepage.html", context)




def get_menu(request):
    context = {
        "svatek": "Marek",
        # SELECT * from Product LIMIT 20;
        "products": Product.objects.all().order_by('name')
    }
    return render(request, "main/menu.html", context)
