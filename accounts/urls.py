from django.urls import path
from .views import loginv , logoutv , registerv

app_name = "accounts"

urlpatterns = [
    path('login/' , loginv , name='login'),
    path('logout/' , logoutv , name='logout'),
    path('register/' , registerv , name='register'),
    
]
