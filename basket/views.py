from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect, HttpResponse
from members.models import Customer
from .forms import BasketForm, AddressForm
from django.contrib import messages
from products.models import Product, Category
from .models import Basket, Coupon


# Create your views here.
@login_required
def create_basket(request):
    try:
        customer = get_object_or_404(Customer, user=request.user)
    except:
        return redirect('accounts:complete-register')

    all_sessions = list(request.session.keys())
    productions = get_list_or_404(Product)
    TotalAmount = []
    if request.method == 'POST':
        basket_form = BasketForm(request.POST)
        address_form = AddressForm(request.POST)
        if basket_form.is_valid():
            basket_instance = basket_form.save()
            basket_instance.customer = customer
            basket_instance.status = 1
            for production in productions:
                if production.name in all_sessions:
                    order_num = request.session[f'numbers_{production.name}']
                    for i in range(int(order_num)):
                        TotalAmount.append(production.price)
                    order_num = int(order_num)
                    production.inventory -= order_num
                    basket_instance.product.add(production)
                    basket_instance.save()
                    production.save()
                    del request.session[f'{production.name}']
                    del request.session[f'numbers_{production.name}']
            basket_instance.total_amount = sum(TotalAmount)
            basket_instance.final_amount = sum(TotalAmount)
            basket_instance.save()
            coupon = Coupon.objects.filter(is_active=True).first()
            if coupon:
                coupon.customers.add(customer)
                messages.success(request,f' : کد تخفیف شما برای خرید بعدی {coupon.coupon_number}')
                coupon.save()
                return redirect('basket:basket')

            return redirect('basket:show-orders')

        elif address_form.is_valid():
            address_instance = address_form.save(commit=False)
            address_instance.customer = customer
            address_instance.save()
            return redirect('basket:basket')
    else:
        basket_form = BasketForm()
        address_form = AddressForm()
        categories = get_list_or_404(Category)

        context = {
            'basket_form': basket_form,
            'categories': categories,
            'address_form': address_form,
        }
        return render(request, 'basket/basket.html', context=context)
@login_required
def show_orders(request):
    try:
        customer = get_object_or_404(Customer, user=request.user)
    except:
        return redirect('accounts:complete-register')
    the_basket = Basket.objects.filter(customer=customer).order_by('-id')
    categories = Category.objects.all()
    context = {
        'the_basket': the_basket,
        'categories': categories
    }
    return render(request, 'basket/show-orders.html', context=context)
@login_required
def last_orders(request):
    try:
        customer = get_object_or_404(Customer, user=request.user)
    except:
        return redirect('accounts:complete-register')
    tha_basket = Basket.objects.filter(customer=customer).order_by('-date')[:10]
    categories = Category.objects.all()
    context = {
        'the_basket': tha_basket,
        'categories': categories
    }
    return render(request, 'basket/last-orders.html', context=context)
# @login_required
# def submitted_addresses(request):
#     try:
#         customer = get_object_or_404(Customer, user=request.user)
#     except:
#         return redirect('accounts:complete-register')
#     the_basket = get_list_or_404(Basket, customer=customer)
#     categories = Category.objects.all()
#     context = {
#         'the_basket': the_basket,
#         'categories': categories
#     }
#     return render(request, 'basket/submitten-addresses.html', context=context)


