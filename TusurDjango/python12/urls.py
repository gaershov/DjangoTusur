"""django_primer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
"""

from django.contrib import admin
from django.urls import path

from .views import IndexView

# Определение маршрутов URL
urlpatterns = [
    # Маршрут для главной страницы
    path('', IndexView.as_view(), name='index'),

    # Маршрут для административной панели
    path('admin/', admin.site.urls),
]
