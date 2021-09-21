from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect

from members.models import Customer
from .models import Product, Category
from basket.models import Basket
from django.contrib import messages

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

@login_required
def order_product(request, pk):
    production = get_object_or_404(Product, id=pk)
    if request.method == 'POST':
        production_name = production.name
        request.session.set_expiry(999999)
        request.session[f'{production_name}'] = production_name
        request.session[f'numbers_{production_name}'] = request.POST['num']
        num = int(request.POST['num'])
        if num > production.inventory:
            messages.error(request,'تعداد مورد نظر از موجودی بیشتر است')
            return redirect('products:detail', pk=production.id)

        messages.success(request, 'با موفقیت به سبد خرید اضافه شد')
        return redirect('products:detail', pk=production.id)
    else:
        messages.error(request, 'مشکلی در اضافه کردن به سبد خرید به وجود آمد')
        return redirect('products:detail', pk=production.id)

def category(request, pk):
    cat = get_object_or_404(Category, id=pk)
    productions = get_list_or_404(Product, category=cat)
    categories = get_list_or_404(Category)
    context = {
        'cat': cat,
        'productions': productions,
        'categories': categories
    }
    return render(request, 'products/category.html', context=context)

@login_required
def show_basket(request):
    list_of_sessions = list(request.session.keys())
    productions = get_list_or_404(Product)
    list_of_basket = []
    for production in productions:
        if production.name in list_of_sessions:
            list_of_basket.append(production.name)
    products = []
    for item in list_of_basket:
        PRODUCTS = get_object_or_404(Product, name=item)
        PRODUCTS.order_number = request.session[f'numbers_{PRODUCTS.name}']
        PRODUCTS.save()
        products.append(PRODUCTS)
    categories = get_list_or_404(Category)
    context = {
        'products': products,
        'categories': categories
    }
    return render(request, 'products/show-basket.html', context=context)

@login_required
def delete_basket_item(request, production_name):
    del request.session[f'{production_name}']
    return redirect('products:show-basket')