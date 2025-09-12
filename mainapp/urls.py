from django.urls import path
from .views import index, merchant, test, pan, home

urlpatterns = [
    path('', index),
    path('merchant', merchant),
    path('test', test),
    path('pan', pan),
    path('home', home)
]

