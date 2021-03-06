from .models import User
from django import forms
from members.models import Customer
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 're_password', 'phone']
        widgets = {
            'password': forms.PasswordInput,
            're_password': forms.PasswordInput,
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "نام کاربری"
        self.fields['password'].label = "کلمه عبور"

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'zip_code']


class ForgetPasswordForm(forms.Form):
    username = forms.CharField(max_length=100, label='نام کاربری')
    phone = forms.CharField(max_length=100, label='شماره تلفن')

class ChangePasswordForm(forms.Form):
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, label='کلمه عبور جدید')
    re_password = forms.CharField(max_length=100, widget=forms.PasswordInput, label='تکرار کلمه عبور جدید')

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'zip_code']

class UserEditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'phone']
