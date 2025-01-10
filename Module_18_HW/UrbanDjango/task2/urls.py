from django.urls import path
from .views import ClassBasedView, function_based_view

urlpatterns = [
    path('class-view/', ClassBasedView.as_view(), name='class_view'),
    path('func-view/', function_based_view, name='func_view'),
]