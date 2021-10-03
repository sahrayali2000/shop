from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from members.models import Customer
from .forms import UserForm, CustomerForm, ForgetPasswordForm, ChangePasswordForm, EditProfileForm, UserEditProfileForm
from django.forms import ValidationError
from django.urls import reverse
# Create your views here.
User = get_user_model()

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
            # if 'next' in request.POST:
            #     return HttpResponseRedirect(request.POST["next"])
            return redirect('products:index')
        else:
            messages.error(request, 'نام کاربری یا کلمه عبور صحیح نیست')
            return render(request, 'accounts/login.html', context={},status=403)
    else:

        return render(request, 'accounts/login.html', context={})
@login_required
def complete_register(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            customer = CustomerForm(request.POST)
            user = request.user
            if customer.is_valid():
                customer_instance = customer.save(commit=False)
                customer_instance.user = user
                customer_instance.save()
                return redirect('accounts:profile')
            else :
                messages.error(request,'مشکلی پیش آمده است')
                return redirect('accounts:complete-register')
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
@login_required
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
@login_required
def change_password(request):
    change_password_form = ChangePasswordForm()
    context = {
        'change_password_form': change_password_form
    }
    return render(request, 'accounts/change_password.html', context=context)
@login_required
def logout_view(request):
    logout(request)
    return redirect('products:index')

@login_required
def edit_profile(request):

    if request.user.is_authenticated:
        try:
            customer = get_object_or_404(Customer, user=request.user)
        except:
            return redirect('accounts:complete-register')
        user = request.user
        user_form = UserEditProfileForm(instance=get_object_or_404(User, username=user.username))
        customer = EditProfileForm(instance=get_object_or_404(Customer, user=user))
        if request.method == 'POST':
            customer = EditProfileForm(request.POST, instance=get_object_or_404(Customer, user=user))
            user_form = UserEditProfileForm(request.POST, instance=get_object_or_404(User, username=user.username))
            if customer.is_valid() and user_form.is_valid():
                customer_instance = customer.save()
                user_instance = user_form.save()
                customer_instance.save()
                user_instance.save()
                messages.success(request, 'ویرایش پروفایل با موفقیت انجام شد')
                return HttpResponseRedirect(reverse('accounts:edit-profile'))
            else:
                messages.error(request, 'ویرایش پروفایل با مشکل مواجه شد')
        else:
            context = {
                'user_form': user_form,
                'customer': customer
            }
            return render(request, 'accounts/edit-profile.html', context=context)



