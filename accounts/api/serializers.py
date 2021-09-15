from rest_framework import serializers
from accounts.models import User
from members.models import Customer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 're_password', 'image', 'phone']


