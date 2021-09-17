from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from members.models import Customer
from .forms import UserForm, CustomerForm, ForgetPasswordForm
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
            try:
                customer = get_object_or_404(Customer, user=request.user)
                return HttpResponse('you cant access this page')
            except:
                user = request.user
                customer = CustomerForm()
                context = {
                    'user': user,
                    'customer': customer,
                }
                return render(request, 'accounts/complete-register.html', context=context)
    else:
        return redirect('accounts:login')

def profile(request):
    if request.user.is_authenticated:
        try:
            customer = get_object_or_404(Customer, user=request.user)
        except:
            return redirect('accounts:complete-register')
        return render(request, 'accounts/profile.html', context={
            'customer': customer
        })
    else:
        return redirect('accounts:login')

def forget_password(request):
    forget_password_form = ForgetPasswordForm()
    context = {
        'forget_password_form': forget_password_form
    }
    return render(request, 'accounts/forget-password.html', context=context)
