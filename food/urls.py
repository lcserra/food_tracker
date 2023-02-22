"""food_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import url
from .views import index, add_meal, delete_meal, update_meal, view_meal, login

urlpatterns = [
    url(r'^$', login, name='login'),
    url(r'^index$', index, name='index'),
    url(r'^add_meal$', add_meal, name='add-meal'),
    url(r'^delete_meal/(?P<meal_id>\d+)$', delete_meal, name='delete-meal'),
    url(r'^update_meal/(?P<meal_id>\d+)$', update_meal, name='update-meal'),
    url(r'^view_meal/(?P<meal_id>\d+)$', view_meal, name='view-meal'),
]

