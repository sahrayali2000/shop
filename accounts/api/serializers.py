from rest_framework import serializers
from accounts.models import User
from members.models import Customer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 're_password', 'phone']

class ForgetPasswordSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    phone = serializers.CharField(max_length=100)

class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=100)
    re_password = serializers.CharField(max_length=100)



