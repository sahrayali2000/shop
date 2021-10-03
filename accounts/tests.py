from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase, Client
from members.models import Customer
from .views import (login_view,logout_view, profile, edit_profile,
                    register, complete_register,
                    forget_password, change_password)
from accounts.api.views import Register
from django.urls import reverse
from products.views import index
from .models import User
from products.models import Product, Category
# Create your tests here.

class TestAuthentication(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username='vahid',password='7607', phone='123456789')
        self.user.save()
        self.category = Category(name='first')
        self.category.save()
        self.product = Product(name='p',category=self.category, discription='a',price=12222, inventory=5)
        self.product.save()
    def test_register_view(self):
        user = Client()
        response = user.post(reverse('authapi:register'),data={
            'username': 'vahidi',
            'password': '7607',
            're_password': '7607',
            'phone': '091555',
        }, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):

        client = Client()
        # client.login(user=self.user)
        response = client.post(reverse('accounts:login'), data={
            'username': 'vahid',
            'password': '7607',
        },follow=True)
        self.assertEqual(response.status_code, 200)

    def test_complete_register(self):
        user = Client()
        response = user.post(reverse('accounts:complete-register'), data={
            'first_name': 'vahidi',
            'last_name': 'vahidii',
        }, follow=True)
        self.assertEqual(response.status_code, 200)

    def test_forget_password(self):
        user = Client()
        response = user.post(reverse('authapi:forget-password'), data={
            'username': 'vahid',
            'phone': '123456789'
        },follow=True)
        self.assertEqual(response.status_code, 200)

    def test_change_password(self):
        user = Client()
        response = user.post(reverse('authapi:change-password'),data={
            'password': '123456',
            're_password': '123456',
            'user': user
        },follow=True)
        self.assertEqual(response.status_code, 200)