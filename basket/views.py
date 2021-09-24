from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_list_or_404, get_object_or_404, redirect, HttpResponse
from members.models import Customer
from .forms import BasketForm
from products.models import Product, Category
from .models import Basket
# Create your views here.
@login_required
def create_basket(request):
    all_sessions = list(request.session.keys())
    customer = get_object_or_404(Customer, user=request.user)
    productions = get_list_or_404(Product)
    TotalAmount = []
    if request.method == 'POST':
        basket_form = BasketForm(request.POST)
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
            return redirect('basket:show-orders')
    else:
        basket_form = BasketForm()
        categories = get_list_or_404(Category)
        context = {
            'basket_form': basket_form,
            'categories': categories,
        }
        return render(request, 'basket/basket.html', context=context)

def show_orders(request):
    customer = get_object_or_404(Customer, user=request.user)
    the_basket = get_list_or_404(Basket, customer=customer)
    categories = Category.objects.all()
    context = {
        'the_basket': the_basket,
        'categories': categories
    }
    return render(request, 'basket/show-orders.html', context=context)

def last_orders(request):
    customer = get_object_or_404(Customer, user=request.user)
    tha_basket = Basket.objects.filter(customer=customer).order_by('-id')[:3]
    categories = Category.objects.all()
    context = {
        'the_basket': tha_basket,
        'categories': categories
    }
    return render(request, 'basket/last-orders.html', context=context)

