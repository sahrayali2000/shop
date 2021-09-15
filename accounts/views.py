from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect
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


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request=request, user=user)
            return HttpResponse('done')
        else:
            return HttpResponse('something wrong')
    else:
        return render(request, 'accounts/login.html', context={})

def complete_register(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            customer = CustomerForm(request.POST)
            user = request.user
            if customer.is_valid():
                customer_instance = customer.save(commit=False)
                customer_instance.user = user
                customer_instance.save()
                return HttpResponse('done')
            else :
                return HttpResponse('something wrong')
        else:
            user = request.user
            customer = CustomerForm()
            context = {
                'user': user,
                'customer': customer,
            }
            return render(request, 'accounts/complete-register.html', context=context)
