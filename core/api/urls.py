from django.urls import path, include

urlpatterns = [
    path('accounts-api/', include('accounts.api.urls')),
    path('basket-api/', include('basket.api.urls')),
]