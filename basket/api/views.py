from django.contrib.auth import authenticate, login
from rest_framework import status, generics, viewsets, permissions, response, mixins
from rest_framework.views import APIView
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from basket.models import Coupon, Basket
from members.models import Customer
from products.models import Product
from .serializers import CouponSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from django.shortcuts import get_object_or_404, get_list_or_404


class CouponApi(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = Coupon
    serializer_class = CouponSerializer

    def post(self, request, *args, **kwargs):
        serializer = CouponSerializer(data=request.data)
        all_sessions = list(request.session.keys())
        customer = get_object_or_404(Customer, user=request.user)
        productions = get_list_or_404(Product)
        TotalAmount = []
        if serializer.is_valid():
            address = serializer.validated_data['address']
            coupon = serializer.validated_data['coupon']
            the_basket = Basket(customer=customer, status=1, address=address)
            the_basket.save()
            for production in productions:
                if production.name in all_sessions:
                    order_num = request.session[f'numbers_{production.name}']
                    for i in range(int(order_num)):
                        TotalAmount.append(production.price)
                    order_num = int(order_num)
                    production.inventory -= order_num
                    the_basket.product.add(production)
                    the_basket.save()
                    production.save()
                    del request.session[f'{production.name}']
                    del request.session[f'numbers_{production.name}']
            the_basket.total_amount = sum(TotalAmount)
            try:
                the_coupon = get_object_or_404(Coupon, customers=customer)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            if the_coupon.coupon_number != coupon:
                print('its wrong')
                return Response(status=status.HTTP_400_BAD_REQUEST)

            the_basket.final_amount = sum(TotalAmount) - (((the_coupon.discount_percent * sum(TotalAmount)) / 100))

            the_basket.save()
            the_coupon.customers.remove(customer)

            the_coupon.save()
            MyData = {'total_amount': the_basket.total_amount, 'final_amount': the_basket.final_amount}
            return Response(data=MyData, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)




