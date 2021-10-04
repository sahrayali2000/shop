from rest_framework import serializers

class CouponSerializer(serializers.Serializer):
    address = serializers.CharField()
    coupon = serializers.IntegerField()
