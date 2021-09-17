from django.urls import path
from .views import register, login_view, complete_register, profile
app_name = 'accounts'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('complete-register/', complete_register, name='complete-register'),
    path('profile/', profile, name='profile')

]