from django.urls import path, include
from .views import CouponApi
from rest_framework.routers import DefaultRouter
app_name = 'couponapi'

urlpatterns = [
    path('coupon/', CouponApi.as_view(), name='coupon'),

]