from rest_framework import status, generics, viewsets, permissions, response, mixins
from rest_framework.views import APIView
from accounts.models import User
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from .serializers import UserSerializer


class Register(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    def post(self, request, *args, **kwargs):

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(serializer.validated_data['password'])
            user.save()

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
