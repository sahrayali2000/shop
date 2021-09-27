from rest_framework import status, generics, mixins
from rest_framework.response import Response
from basket.models import Coupon, Basket
from members.models import Customer
from products.models import Product
from .serializers import CouponSerializer
from datetime import date, datetime
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
            try:
                the_coupon = Coupon.objects.get(customers=customer, is_active=True)
            except:
                return Response(status=status.HTTP_400_BAD_REQUEST)

            today = datetime.today()
            expire_date = str(the_coupon.expire_date)
            expire_date = datetime.strptime(expire_date, '%Y-%m-%d')
            if today > expire_date:
                the_coupon.is_active = False
                the_coupon.save()
                return Response(status=status.HTTP_400_BAD_REQUEST)
            if the_coupon.coupon_number != coupon:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            the_basket = Basket(customer=customer, status=1, address=address)
            the_basket.save()
            MyData = dict()
            for production in productions:
                if production.name in all_sessions:
                    order_num = request.session[f'numbers_{production.name}']
                    response_data = {f'{production.name}' : order_num}
                    MyData.update(response_data)
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
            the_basket.final_amount = sum(TotalAmount) - (((the_coupon.discount_percent * sum(TotalAmount)) / 100))
            MyData.update({'total_amount': the_basket.total_amount, 'final_amount': the_basket.final_amount,})
            the_basket.save()
            the_coupon.customers.remove(customer)
            the_coupon.save()
            return Response(data=MyData, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)




