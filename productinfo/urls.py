from django.contrib import admin
from django.urls import path
from .views import productinfo
urlpatterns=[

    path('productinfo',productinfo)


]
