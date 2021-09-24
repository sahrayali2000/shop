from rest_framework import serializers
from basket.models import Basket, Coupon

class CouponSerializer(serializers.Serializer):
    address = serializers.CharField()
    coupon = serializers.IntegerField()
