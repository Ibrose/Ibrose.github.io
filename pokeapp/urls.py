"""pokeconfig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import include, url
from django.urls import path
from . import views as pokeviews
from .views import arceus
from flask import request
urlpatterns = [
    
    path('', pokeviews.arceus.as_view(name = 'ddd')),
    #path('/initAction', pokeviews.arceus.initAction),#initAction an
    path('/pokeinput', pokeviews.arceus.get),
    #path('', pokeviews.arceus.as_view(request)),
    
    
]