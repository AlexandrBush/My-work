from django.urls import path
from . import views

# Определяем список маршрутов (URL-адресов) для приложения
urlpatterns = [
    # Маршрут для корневого URL (''), который будет обрабатываться функцией sign_up_by_html
    # name='sign_up_by_html' — имя маршрута, которое можно использовать для ссылок в шаблонах
    path('', views.sign_up_by_html, name='sign_up_by_html'),

    # Маршрут для URL 'django_sign_up/', который будет обрабатываться функцией sign_up_by_django
    # name='sign_up_by_django' — имя маршрута, которое можно использовать для ссылок в шаблонах
    path('django_sign_up/', views.sign_up_by_django, name='sign_up_by_django'),
]