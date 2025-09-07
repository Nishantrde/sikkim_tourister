from django.urls import path
from .views import index, merchant

urlpatterns = [
    path('', index),
    path('merchant', merchant)
]

