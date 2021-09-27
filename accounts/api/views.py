from django.contrib.auth import authenticate, login
from rest_framework import status, generics, viewsets, permissions, response, mixins
from rest_framework.views import APIView
from accounts.models import User
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .serializers import UserSerializer, ForgetPasswordSerializer, ChangePasswordSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404
class Register(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser, FormParser]
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data['password'] == serializer.validated_data['re_password']:
                user = serializer.save()
                user.set_password(serializer.validated_data['password'])
                user.save()
                user_instance = authenticate(request, username=serializer.validated_data['username'], password=serializer.validated_data['password'])
                login(request, user=user_instance)
                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class ForgetPasswordApi(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = ForgetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = ForgetPasswordSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            phone = serializer.validated_data['phone']
            try:
                user = get_object_or_404(User, username=username, phone=phone)
                authenticate(request, username=username, password=user.password)
                if user is not None:
                    login(request, user=user)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            return Response(status=status.HTTP_200_OK)

class ChangePasswordApi(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = ChangePasswordSerializer

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            serializer = ChangePasswordSerializer(data=request.data)
            user = request.user
            if serializer.is_valid():
                password = serializer.validated_data['password']
                re_password = serializer.validated_data['re_password']
                if password == re_password:
                    user.set_password(password)
                    user.save()
                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

####

# @register.filter(name='en_to_fa')
# def en_to_fa(text):
#     """convert english number to persian"""
#     fa_numbers = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹']
#     text_list = list(str(text))
#     for i in range(len(text_list)):
#         if text_list[i].isnumeric():
#             text_list[i] = fa_numbers[int(text_list[i])]
#     return ''.join(text_list)
# register = template.Library()