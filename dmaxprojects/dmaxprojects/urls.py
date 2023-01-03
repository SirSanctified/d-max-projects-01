"""
dmaxprojects URL Configuration

The `urlpatterns` list routes URLs to views.
"""

from django.contrib import admin
from django.urls import path
from . import settings
from django.contrib.staticfiles.urls import static
from main.views import home, services, contact, gallery

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('services/', services),
    path('contact/', contact),
    path('gallery/', gallery),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
