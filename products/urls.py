from django.urls import path
from .views import index, product_detail
app_name = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:pk>/', product_detail, name='detail')

]