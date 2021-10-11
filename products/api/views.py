from django.contrib.auth import authenticate, login
from rest_framework import status, generics, viewsets, permissions, response, mixins
from rest_framework.views import APIView
from accounts.models import User
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .serializers import SearchSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404, get_list_or_404
from products.models import Product, Category


class Search(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = SearchSerializer

    def post(self,request , *args, **kwargs):
        search_serializer = SearchSerializer(data=request.data)
        if search_serializer.is_valid():
            try:
                search_instance = get_list_or_404(Product, name__contains=search_serializer.validated_data['search_input'])
                MyData = dict()
                for item in search_instance:
                    MyData.update({f'{item.name}': item.id})

                data = {'product': MyData}
                return Response(data=data, status=status.HTTP_200_OK)
            except:
                try:
                    search_instance = get_object_or_404(Category, name__contains=search_serializer.validated_data['search_input'])
                    data = {'category': {f'{search_instance.name}': search_instance.id}}
                    return Response(data=data, status=status.HTTP_200_OK)
                except:
                    return Response(status=status.HTTP_400_BAD_REQUEST)



