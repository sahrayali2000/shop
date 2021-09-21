from django.urls import path
from .views import index, product_detail, order_product, show_basket, delete_basket_item
app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>/', product_detail, name='detail'),
    path('order-product/<int:pk>/', order_product, name='order-product'),
    path('show-basket/', show_basket, name='show-basket'),
    path('delete-basket-item/<str:production_name>', delete_basket_item, name='delete-basket-item')

]