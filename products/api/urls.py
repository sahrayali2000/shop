from django.urls import path, include
from .views import Search
app_name = 'productapi'

urlpatterns = [
    path('search/', Search.as_view(), name='search'),

]