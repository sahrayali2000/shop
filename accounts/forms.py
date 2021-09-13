from .models import User
from django import forms
from members.models import Customer
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 're_password', 'image', 'phone']
        widgets = {
            'password': forms.PasswordInput,
            're_password': forms.PasswordInput,
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'zip_code']
