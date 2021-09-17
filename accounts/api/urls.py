from django.urls import path, include
from .views import Register, ForgetPasswordApi, ChangePasswordApi
from rest_framework.routers import DefaultRouter
app_name = 'authapi'
router = DefaultRouter()
router.register(r'', Register, basename='registerapi')
urlpatterns = [
    # path('register/', include(router.urls), name='register-customer')
    path('register/', Register.as_view(), name='register'),
    path('forget-password', ForgetPasswordApi.as_view(), name='forget-password'),
    path('change-password/', ChangePasswordApi.as_view(), name='change-password')

]
