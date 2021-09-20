from django.shortcuts import render, get_list_or_404
from .models import Product, Category
# Create your views here.

def index(request):
    list_of_products = get_list_or_404(Product)
    categories = get_list_or_404(Category)
    context = {
        'products': list_of_products,
        'categories': categories
    }
    return render(request, 'products/index.html', context=context)