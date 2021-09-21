from django.urls import path
from .views import create_basket
app_name = 'basket'

urlpatterns = [
    path('basket/', create_basket, name='basket'),
]