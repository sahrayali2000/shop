from random import randint

from django.contrib.auth.decorators import login_required
from django.core import paginator
from django.core.paginator import PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect

from members.models import Customer
from .models import Product, Category
from basket.models import Basket
from django.contrib import messages

# Create your views here.

def index(request):
    list_of_products = paginator.Paginator(Product.objects.all().order_by('-id'), 6)
    page = request.GET.get('page',1)
    try:
        list_of_products = list_of_products.page(page)
    except PageNotAnInteger:
        list_of_products = list_of_products.page(1)
    except EmptyPage:
        list_of_products = list_of_products.page(list_of_products.num_pages)

    categories = get_list_or_404(Category)
    newest_products = Product.objects.all().order_by('-id')[:4]

    products_len = len(Product.objects.all())
    second_num = randint(4, products_len)
    first_num = second_num - 4

    recommendedـproducts = Product.objects.all().order_by('id')[first_num:second_num]
    context = {
        'products': list_of_products,
        'categories': categories,
        'newest_products': newest_products,
        'recommendedـproducts': recommendedـproducts,
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
    list_of_sessions = list(request.session.keys())
    if request.method == 'POST':
        production_name = production.name
        num = int(request.POST['num'])
        if num > production.inventory:
            messages.error(request,'تعداد مورد نظر از موجودی بیشتر است')
            return redirect('products:detail', pk=production.id)
        if production_name in list_of_sessions:
            request.session[f'numbers_{production_name}'] += request.POST['num']
        request.session.set_expiry(999999)
        request.session[f'{production_name}'] = production_name
        request.session[f'numbers_{production_name}'] = request.POST['num']
        messages.success(request, 'با موفقیت به سبد خرید اضافه شد')
        return redirect('products:detail', pk=production.id)
    else:
        return redirect('products:detail', pk=production.id)

def category(request, pk):
    cat = get_object_or_404(Category, id=pk)
    productions = paginator.Paginator(Product.objects.filter(category=cat).order_by('-id'), 6)
    page = request.GET.get('page',1)

    try:
        productions = productions.page(page)
    except PageNotAnInteger:
        productions = productions.page(1)
    except EmptyPage:
        productions = productions.page(productions.num_pages)

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
        products.append(PRODUCTS)
    categories = get_list_or_404(Category)
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'products/show-basket.html', context=context)

@login_required
def delete_basket_item(request, production_name):
    del request.session[f'{production_name}']
    return redirect('products:show-basket')