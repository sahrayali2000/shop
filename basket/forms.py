from django import forms
from .models import Basket, Address

class BasketForm(forms.ModelForm):
    class Meta:
        model = Basket
        fields = ['address']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['title', 'address_content']


