"""
URL configuration for gym_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from core.views import home_page, login_view, register_page, submit_trial_booking

urlpatterns = [
    path('django-admin/', admin.site.urls),
    path('', home_page, name='home'),
    path('login/', login_view, name='login'),
    path('register/', register_page, name='register'),
    path('trial-booking/', submit_trial_booking, name='submit_trial'),
    path('dashboard/', include('core.admin_urls')),
    path('api/', include('core.urls')),
]
