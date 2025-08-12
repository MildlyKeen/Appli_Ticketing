"""Appli_Ticketing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Import the views.py file from the current directory.
# We're using 'as main_views' to avoid any name conflicts.
from . import views as main_views

urlpatterns = [
    # This line tells Django that the root URL ('') should be handled by the 'home' view
    # from the main project's views.py file.
    path('', main_views.home, name='home'),
    path('admin/', admin.site.urls),
    path('tickets/', include('tickets.urls')),
]
