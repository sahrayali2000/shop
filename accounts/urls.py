from django.urls import path
from .views import register, login_view, complete_register, profile, forget_password, change_password, edit_profile, logout_view
app_name = 'accounts'
urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('complete-register/', complete_register, name='complete-register'),
    path('profile/', profile, name='profile'),
    path('forget-password/', forget_password, name='forget_password'),
    path('change-password/', change_password, name='change_password'),
    path('edit-profile/', edit_profile, name='edit-profile'),
    path('logout/', logout_view, name='logout')

]