from django.shortcuts import render
from .forms import UserForm, CustomerForm
from django.forms import ValidationError
# Create your views here.

def register(request):
    if request.method == 'POST':
        customer = CustomerForm(request.POST)
        user = UserForm(request.POST)
        if user.password != user.re_password:
            raise ValidationError('پسورد و تکرار پسورد یکسان نیست')
        if customer.is_valid() and user.is_valid():
            customer_instance = customer.save(commit=False)
            user_instance = user.save()
            user_instance.set_password(user_instance.password)
            user_instance.save()
            customer_instance.user = user_instance
            customer_instance.save()
            context = {
                'success': 'ثبت نام با موفقیت انجام شد',
            }
            return render(request, 'accounts/register.html', context=context)
        else:
            context = {
                'error': 'مشکلی در ثبت نام وجود دارد',
            }
            return render(request, 'accounts/register.html', context=context)
    else:
        customer = CustomerForm()
        user = UserForm()
        context = {
            'customer': customer,
            'user': user
        }
        return render(request, 'accounts/register.html', context=context)