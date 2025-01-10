from django.urls import path
from . import views

urlpatterns = [
    path('', views.platform, name='platform'),
    path('games/', views.games, name='games'),
    path('cart/', views.cart, name='cart'),
]