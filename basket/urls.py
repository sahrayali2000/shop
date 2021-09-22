from django.urls import path
from .views import create_basket, show_orders
app_name = 'basket'

urlpatterns = [
    path('basket/', create_basket, name='basket'),
    path('show-orders/', show_orders, name='show-orders'),
]