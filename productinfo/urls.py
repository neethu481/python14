from django.contrib import admin
from django.contrib import admin
from django.urls import path
from .views import productinfo, productlist


urlpatterns = [
    path ('productinfo', productinfo ),
    path ('productlist', productlist ),
]
