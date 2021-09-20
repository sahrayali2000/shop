from django.shortcuts import render, get_list_or_404, get_object_or_404
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

def product_detail(request, pk):
    categories = get_list_or_404(Category)
    my_product = get_object_or_404(Product, id=pk)
    context = {
        'my_product': my_product,
        'categories': categories
    }
    return render(request, 'products/detail.html', context=context)
