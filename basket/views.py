from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Basket
# Create your views here.
@login_required
def create_basket(request):
    print(request.session.keys())
    return render(request, 'basket/basket.html', context={})