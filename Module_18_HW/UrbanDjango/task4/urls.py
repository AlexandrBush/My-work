from django.urls import path
from . import views

urlpatterns = [
    path('', views.platform, name='platform'),  # Главная страница
    path('games/', views.games, name='games'),  # Магазин игр
    path('cart/', views.cart, name='cart'),  # Корзина
]